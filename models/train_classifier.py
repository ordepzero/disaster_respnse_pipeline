import sys

import pandas as pd
from sqlalchemy import create_engine
import nltk
import joblib 
import re
import time

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download(['punkt', 'wordnet','stopwords'])

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def load_data(database_filepath='messages_categories.db',table_name='messages_categories',column_name='message'):
    engine = create_engine('sqlite:///'+database_filepath)
    df = pd.read_sql(table_name,con=engine)

    X = df[column_name]
    Y = df[df.columns[5:]]
    
    return X,Y,Y.columns


def tokenize(text):
    # normalize text and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)
    stop_words = stopwords.words("english")
    words = [w for w in tokens if w not in stop_words]
    
    # Reduce words to their stems
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in words]
    
    # Reduce words to their root form
    lemmatizer = WordNetLemmatizer()
    lemmed = [lemmatizer.lemmatize(w) for w in stemmed]
    
    return lemmed


def build_model():
    pipeline = Pipeline([
    ('vect',CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf',MultiOutputClassifier(RandomForestClassifier(n_jobs=-1)))])

    return pipeline

def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    print(classification_report(Y_test, y_pred, target_names=category_names))

def save_model(model, model_filepath='random_forest.pkl'):
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()