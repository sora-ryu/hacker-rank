# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
# from sklearn.linear_model import LinearRegression, LogisticRegression # Cannot use sklearn module

physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

# history = a * physics + b
# a = slope obtained from second question
# b = history - a * physics

def mean(data):
    return sum(data)/len(data)

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

cov, std_physics = 0, 0
for i in range(len(physics)):
    cov += (physics[i]-mean(physics)) * (history[i]-mean(history))
    std_physics += (physics[i]-mean(physics)) ** 2
    
slope = cov / std_physics
bias = mean(history) - slope * mean(physics)

print(round(slope * 10 + bias, 1))
