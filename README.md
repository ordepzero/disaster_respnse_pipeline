# Disaster Response Pipeline Project


## Table of Contents
1. [Introduction](#introduction)
2. [Objetives](#objetives)
3. [Description](#description)
4. [Getting Started](#getting_started)
	1. [Create Virutal Enviroment](#env)
	2. [Dependencies](#dependencies)
	3. [Installing dependences](#installing)
	4. [Clone Repository](#clone)
	5. [Executing Program](#executing)
5. [File Structure](#files)
6. [Authors](#authors)
7. [License](#license)
8. [Acknowledgement](#acknowledgement)

<a name="descripton"></a>
## Introduction

After a disaster, responsible agencies typically receive millions of direct or social media communications
just when disaster response organizations are least able to filter
and select the most important messages. Often, only one in a thousand messages is
relevant for disaster response professionals. Typically, in response to disasters,
Different organizations take care of different parts of the problem. One organization takes care of water, another takes care of blocked roads,
another takes care of medical supplies.

<a name="objectives"></a>
## Objectives

This Project is a part of Data Science Nanodegree Program by Udacity in 
collaboration with Figure Eight. This project aims to develop a computational 
model based on the Natural Language Processing (NLP) to classify messages and 
identify needs after a disaster.

<a name="description"></a>
## Description

When looking at the data, these are the categories that have selected for the 
data set.
The Figure Eight is used for many of the disasters from which messages were 
pulled, then combined the data sets and re-labeled them
to have consistent labels across different disasters. 
This is to allow to investigate the different trends that can found
and build supervised machine learning models to help respond to future disasters.
The aim of the project is to build a Natural Language Processing (NLP) tool that categorize disaster messages.

The Project is divided in the following Sections:

1. Data Processing, ETL Pipeline to extract data from source, clean data and save them in a proper database structure.
2. Machine Learning Pipeline to train and tunning a model able to classify text messages into appropriate categories.
3. Web App to show model results in real time. 

<a name="getting_started"></a>
## Getting Started

<a name="env"></a>
## Create Virutal Enviroment (Windows)


 `$ python -m venv disaster_env`

 `$ disaster_env\Scripts\activate`

<a name="dependencies"></a> 
## Dependences

	click==7.1.2
	Flask==1.1.2
	itsdangerous==1.1.0
	Jinja2==2.11.2
	joblib==0.16.0
	MarkupSafe==1.1.1
	nltk==3.5
	numpy==1.19.1
	pandas==1.1.1
	plotly==4.9.0
	python-dateutil==2.8.1
	pytz==2020.1
	regex==2020.7.14
	retrying==1.3.3
	scikit-learn==0.23.2
	scipy==1.5.2
	six==1.15.0
	SQLAlchemy==1.3.19
	threadpoolctl==2.1.0
	tqdm==4.48.2
	Werkzeug==1.0.1

<a name="installing"></a>
## Installing dependences

`$ pip install -r requirements.txt`

<a name="clone"></a>
## Clone repository

Clone this GIT repository:

```
git clone https://github.com/ordepzero/disaster_respnse_pipeline
```

<a name="executing"></a>
### Executing Program:
	1. Run the following commands in the project's root directory to set up your database and model.

		a) To run ETL pipeline that cleans data and stores in database
	
			`$ python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db`
		
		b) To run ML pipeline that trains classifier and saves

			`$ python models/train-classifier.py data/DisasterResponse.db model/DS_model.pkl`
	
	2. Run the following command in the app's directory to run your web app. 

		`$ python run.py`

	3. Go to localhost:5000/


<a name="file"></a>
## File Structure

* `../data/run.py` is the executable for the app
* `requirements.txt`: contains the environment requirements to run program
* `app` folder contains the following:
  * `templates`: Folder containing
    * `index.html`: Renders homepage
    * `go.html`: Renders the message classifier
  * `run.py`: Defines the app routes
* `data` folder contains the following:
    * `disaster_categories.csv`: contains the disaster categories csv file
    * `disaster_messages.csv`: contains the disaster messages csv file
    * `DisasterResponse.db`: contains the emergency db which is a merge of categories and messages by ID
    * `process_data.py`: contains the scripts to transform data  
* `models` folder contains the following:
    * `random_forest.pkl`: contains the RandomForestClassifier pickle file
    * `train_classifier.py`: script to train ml_ipeline.py


<a name="authors"></a>
## Authors

* [ordepzero](https://github.com/ordepzero)

<a name="license"></a>

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<a name="acknowledgement"></a>

## Acknowledgements

* [Udacity](https://www.udacity.com/) for providing such a complete Data Science Nanodegree Program
* [Figure Eight](https://www.figure-eight.com/) for providing messages dataset to train my model


