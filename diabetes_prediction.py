# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tAhXM_boGlpBq7caIp66i9RMD0ucGmyN
"""



"""Importing dependencies"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Dataset Collection

"""

#loading diabetes dataset to pandas
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

pd.read_csv?

#printing the first 5 rows
diabetes_dataset.head()

#Number of rows and columns
diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-diabetic
1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

#seperating data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

X = standardized_data
Y = diabetes_dataset['Outcome']
print(X)
print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify = Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training model"""

classifier = svm.SVC(kernel='linear')

#Training the support vector machine classifier
classifier.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

#Accuracy Score
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of training data - ', training_data_accuracy)

#Accuracy Score for test data
X_test_prediction = classifier.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of testing data - ', testing_data_accuracy)

"""Making Predictive System"""

input_data = (4,110,92,0,0,37.6,0.191,30)

#changing input to numpy array
input_data_numpy_array = np.asarray(input_data)

# reshape the array for prediction of the instance
input_data_reshaped = input_data_numpy_array.reshape(1,-1)

#standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

#prediction
prediction = classifier.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

