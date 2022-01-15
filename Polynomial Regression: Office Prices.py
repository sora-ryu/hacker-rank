# Enter your code here. Read input from STDIN. Print output to STDOUT

# Import libraries
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

num_features, num_rows = map(int, input().split(" "))

X_train, y_train = [], []
for i in range(num_rows):
    sample = list(map(float, input().split(" ")))
    X_train.append(sample[:-1])
    y_train.append(sample[-1])

# print(X_train) # [[0.44, 0.68], [0.99, 0.23], ... ]

# transforms the existing features to higher degree features.
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train)

# fit the transformed features to Linear Regression
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

num_test = int(input())
X_test = []
for i in range(num_test):
    sample = list(map(float, input().split(" ")))
    X_test.append(sample)

y_predicted = poly_model.predict(poly_features.fit_transform(X_test))

for i in range(len(y_predicted)):
    print(round(y_predicted[i], 2))
