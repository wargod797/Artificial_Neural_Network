# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:05:27 2019

@author: sridhar
"""
#Importing the Libararies
import pandas as pd
import keras 
from  keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

#Encoding Catagorical data
label_encoder_1 = LabelEncoder()
X[:, 1] = label_encoder_1.fit_transform(X[:, 1])
label_encoder_2 = LabelEncoder()
X[:, 2] = label_encoder_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Creating a Artifical Neural Network Model

classifier = Sequential()

#Adding First layer to ANN Model

classifier.add(Dense(units = 6, kernel_initializer='uniform', activation='relu', input_dim = 11))

#Adding the Second Layer

classifier.add(Dense(units = 6, kernel_initializer='uniform', activation='relu'))

#Adding the Output Layer 

classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 25)

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



