# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

img = input().split(" ") # ['195,89,1', '195,89,1', ... ]
brightness = 0

for pixel in img:
    channel = [int(x) for x in pixel.split(",")]
    brightness += np.sum(channel) / 3
    
if brightness / len(img) > 90:
    print("day")
else:
    print("night")
    
