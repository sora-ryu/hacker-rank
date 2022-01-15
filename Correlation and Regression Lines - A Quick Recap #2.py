# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def mean(data):
    return sum(data)/len(data)

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

cov, std_physics = 0, 0
for i in range(len(physics)):
    cov += (physics[i]-mean(physics)) * (history[i]-mean(history))
    std_physics += (physics[i]-mean(physics)) ** 2
    
slope = cov / std_physics
print(round(slope, 3))
