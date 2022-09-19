#Import required libraries 
import tensorflow

import keras #library for neural network
import pandas as pd #loading data in table form  
import seaborn as sns #visualisation 
import matplotlib.pyplot as plt #visualisation
import numpy as np # linear algebra

from tkinter import E
from sklearn.preprocessing import normalize #machine learning algorithm library
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from keras.utils import np_utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout 
from tensorflow.keras.models import save_model, load_model



class ANN(object):

    def __init__(self) -> None:
        self.X_train, self.X_test, self.y_train, self.y_test = self._prepare_data()

    def _read_data_soruce(self, csv_file="https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"):
        # iris_dataset=pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
        if csv_file:
            iris_dataset = pd.read_csv(csv_file)

            iris_dataset.loc[iris_dataset["species"] == "setosa", "species"] = 0
            iris_dataset.loc[iris_dataset["species"] == "versicolor", "species"] = 1
            iris_dataset.loc[iris_dataset["species"] == "virginica", "species"] = 2
        else:
            pass
        return iris_dataset

    def _prepare_data(self):

        iris_dataset = self._read_data_soruce()
        # Break the dataset up into the examples (X) and their labels (y)
        X = iris_dataset.iloc[:, 0:4].values
        y = iris_dataset.iloc[:, 4].values
        X = normalize(X, axis=0)

        # Split up the X and y datasets randomly into train and test sets
        # 20% of the dataset will be used for the test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=31)

        # Change the label to one hot vector
        '''
        [0]--->[1 0 0]
        [1]--->[0 1 0]
        [2]--->[0 0 1]
        '''
        y_train = np_utils.to_categorical(y_train, num_classes=3)
        y_test = np_utils.to_categorical(y_test, num_classes=3)

        return (X_train, X_test, y_train, y_test)

    def _build_model(self):
        # Initialising the ANN
        model = Sequential()

        # Adding the input layer and the first hidden layer
        model.add(Dense(1000, input_dim=4, activation='relu'))
        # Changing number of nodes in first hidden layer
        model.add(Dense(50, activation='relu'))

        # Adding the second hidden layer
        model.add(Dense(300, activation='relu'))
        # Protects against overfitting
        model.add(Dropout(0.2))

        # Adding the output layer
        model.add(Dense(3, activation='softmax'))

        # Compiling the ANN
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # # Fitting the ANN to the Training set
        # model.fit(X_train,y_train,validation_data=(X_test,y_test),batch_size=20,epochs=10,verbose=1)

        return model

    def _training_model(self, save_path):
        X_train, X_test, y_train, y_test = self._prepare_data()
        # Fitting the ANN to the Training set
        model = self._build_model()
        model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=20, epochs=10, verbose=1)
        self._save_model(model, save_path)
        return model

    def predict_all(self, model):
        # Predicting the Test set results
        y_pred = model.predict(self.X_test)
        y_pred = (y_pred > 0.5)

        prediction = model.predict(self.X_test)
        length = len(prediction)
        y_label = np.argmax(self.y_test, saxis=1)
        predict_label = np.argmax(prediction, axis=1)
        # how times it matched/ how many test cases
        accuracy = np.sum(y_label == predict_label)/length * 100
        print("Accuracy of the dataset", accuracy)

    def predict_one(self, model, data):
        pickled_model = self._load_model()
        # predict one
        pickled_prediction = pickled_model.predict(np.array([data[0]]))
        predict_label = np.argmax(pickled_prediction, axis=1)
        print("predict_prediction = ", predict_label)

    def _save_model(self, model, filepath):
        save_model(model, filepath, "model.h5")

    def _load_model(self, path):
        # load model
        model = load_model('model.h5')
        return model