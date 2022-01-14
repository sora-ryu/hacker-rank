# # Enter your code here. Read input from STDIN. Print output to STDOUT

# import math
# import numbers

# def karl_pearson(score1, score2):
#     coefficient = 0.0
#     mean1, mean2, std1, std2 = 0, 0, 0, 0
    
#     for i in range(len(score1)):
#         mean1 += score1[i]
#         mean2 += score2[i]
        
#     mean1 /= len(score1)
#     mean2 /= len(score2)
    
#     for i in range(len(score1)):
#         coefficient += (score1[i] - mean1) * (score2[i] - mean2)
#         std1 += (score1[i] - mean1)**2
#         std2 += (score2[i] - mean2)**2
    
#     coefficient /= math.sqrt(std1) * math.sqrt(std2)
    
#     return coefficient

# # score1 = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
# # score2 = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# score1 = input() # get line by line
# score2 = input()
# score1 = [int(x) for x in score1.split() if x.isdigit()]
# score2 = [int(x) for x in score2.split() if x.isdigit()]
    
# r = karl_pearson(score1, score2)
# #print('{0:.3f}'.format(r))
# print(round(r, 3))

# Import library
import math as m

# Define functions
def mean(data):
    return sum(data) / len(data)

def var(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - mean(data)) ** 2
    return sum

def cov(dt1, dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - mean(dt1)) * (dt2[i] - mean(dt2))
    return sum

# Set data
physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

mean_physics = mean(physics)
mean_history = mean(history)

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = m.sqrt(var_physics * var_history)

# Correlation
r = cov / std
print(round(r, 3))
