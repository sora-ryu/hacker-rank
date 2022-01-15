# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

num_integers = int(input())
integers = sorted(list(map(float, input().split(" "))))

mean = sum(integers) / num_integers

if num_integers % 2 != 0:
    median = integers[num_integers//2]
else:
    median = (integers[num_integers//2 - 1] + integers[num_integers//2]) / 2

mode = integers[0]

std = 0.0
for integer in integers:
    std += (integer - mean) ** 2
std /= num_integers
std = math.sqrt(std)

# 95% Confidence Interval for the mean: (m - 0.95*s/sqrt(N), m + 0.95*s/sqrt(N))
confidence = 0.95
boundaries = str(round(mean - (1.96*std/math.sqrt(num_integers)), 1)) + " " + str(round(mean + (1.96*std/math.sqrt(num_integers)), 1))

print(round(mean, 1))
print(round(median, 1))
print(int(mode))
print(round(std, 1))
print(boundaries)
