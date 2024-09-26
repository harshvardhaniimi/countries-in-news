# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 02:04:30 2016

@author: DIP
"""

import pandas as pd
dataset = pd.read_csv('movie_reviews.csv')
print(dataset.shape)
print(dataset.head())

dataset['sentiment'].value_counts()

#%% Prepare Data

# feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(dataset['review'])
feature_matrix

# data partitioning
from sklearn.model_selection import train_test_split
train_features, test_features, train_sentiments, test_sentiments = train_test_split(feature_matrix, 
                                                dataset['sentiment'], 
                                                random_state=1)

#%% build the model
from sklearn.linear_model import SGDClassifier
svm = SGDClassifier(loss='hinge')
svm.fit(train_features, train_sentiments)

# apply to test set
predicted_sentiments = svm.predict(test_features)       

# check performance
from sklearn.metrics import confusion_matrix
confusion_matrix(predicted_sentiments, test_sentiments)

