# Enter your code here. Read input from STDIN. Print output to STDOUT
# Pearson Correlation Coefficient
# https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

import math as m

num_rows = int(input())

# Define functions
def mean(data):
    return sum(data) / len(data)

def var(data, mean_data):
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - mean_data) ** 2
    return sum

def cov(dt1, dt2, mean_dt1, mean_dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - mean_dt1) * (dt2[i] - mean_dt2)
    return sum

math, physics, chemistry = [], [], []
for i in range(num_rows):
    row = list(map(int, input().split("\t")))
    math.append(row[0])
    physics.append(row[1])
    chemistry.append(row[2])

mean_math = mean(math)
mean_physics = mean(physics)
mean_chemistry = mean(chemistry)

var_math = var(math, mean_math)
var_physics = var(physics, mean_physics)
var_chemistry = var(chemistry, mean_chemistry)

cov_mp = cov(math, physics, mean_math, mean_physics)
cov_pc = cov(physics, chemistry, mean_physics, mean_chemistry)
cov_cm = cov(chemistry, math, mean_chemistry, mean_math)

std_mp = m.sqrt(var_math * var_physics)
std_pc = m.sqrt(var_physics * var_chemistry)
std_cm = m.sqrt(var_chemistry * var_math)

# Correlation
print(round(cov_mp/std_mp, 2))
print(round(cov_pc/std_pc, 2))
print(round(cov_cm/std_cm, 2))
