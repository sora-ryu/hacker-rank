# Enter your code here. Read input from STDIN. Print output to STDOUT
# Import Libraries
from sklearn.linear_model import LinearRegression

# Prepare Dataset
X_train, y_train, X_test = [], [], []

num_features, num_rows = map(int, input().split(" "))
for i in range(num_rows):
    sample = list(map(float, input().split(" ")))
    X_train.append(sample[:-1])
    y_train.append(sample[-1])

num_test = int(input())
for i in range(num_test):
    sample = list(map(float, input().split(" ")))
    X_test.append(sample)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the Model
y_predicted = model.predict(X_test)
for i in range(len(y_predicted)):
    print(round(y_predicted[i], 2))
