#!/bin/python3

import math
import os
import random
import re
import sys
from sklearn.linear_model import LinearRegression, LogisticRegression
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


# Set dataset to training
dataset = pd.read_csv('trainingdata.txt', header=None)

# Plot the graph with the data
# plt.plot(dataset.iloc[:,0], dataset.iloc[:,1], 'ro')
# plt.ylabel('Laptob Battery Life')
# plt.show()

# According to the chart, we must remove items with a 
# duration of time greater than eight.
dataset = dataset[dataset.iloc[:,1] < 8]

# Add bias
dataset.insert(0, len(dataset.columns), 0)

# Separe variables dependent and independent
X_train = dataset.iloc[:,0:2].to_numpy()
y_train = dataset.iloc[:,2].to_numpy()

# Create the classifier model
model = LinearRegression()
model.fit(X_train, y_train)

# Set new value to predict
timeCharged = float(input().strip())
result = model.predict([[0, timeCharged]])
if result[0] > 8:
    print (8.0)
else:
    print (round(result[0],2))
# if __name__ == '__main__':
#     timeCharged = float(input().strip())   # X_test
    
#     # Prepare dataset
#     X_train, y_train = [], []
#     with open("trainingdata.txt") as f:
#         f.readline()
#         for line in f:
#             time_charged, time_lasted = line.split(",")
#             X_train.append([0.0, float(time_charged)])
#             y_train.append(float(time_lasted))
    
#     X_train = [X_train]
    
#     # Regression
#     classifier = LinearRegression()
#     classifier.fit(X_train, y_train)
    
#     # Set new value to predict
#     result = classifier.predict([[0, timeCharged]])
#     if result[0] > 8:
#         print (8.0)
#     else:
#         print (round(result[0],2))
