import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath='disaster_messages.csv', categories_filepath='disaster_categories.csv'):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    return messages.merge(categories, left_on='id', right_on='id')


def clean_data(df):
    genre_dummies = pd.get_dummies(df['genre'])
    categories = df['categories'].str.split(';',expand=True)
    
    row = map(lambda x: x.split('-')[0], categories.iloc[0])

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = list(row)
    categories.columns = category_colnames
    
    for column in categories.columns:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x:x.split('-')[1])
    
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    categories.loc[categories['related'] == 2,'related'] = 1
    
    df = df.drop(['categories'], axis=1)
    df = df.join(categories)

    df = df.drop_duplicates()
    
    return df


def save_data(df, database_filename='messages_categories.db',table_name='messages_categories'):
    dbpath = 'sqlite:///'+database_filename
    table = table_name
    engine = create_engine(dbpath)
    connection = engine.raw_connection()
    cursor = connection.cursor()
    command = "DROP TABLE IF EXISTS {};".format(table)
    cursor.execute(command)
    connection.commit()
    cursor.close()  
    
    engine = create_engine(dbpath)
    df.to_sql(table, engine, index=False)


def main():
    print(len(sys.argv))
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')
        print(sys.argv[1:])


if __name__ == '__main__':
    main()