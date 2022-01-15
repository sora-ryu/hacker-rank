var_x = float(input()) ** 2
# y = (20*x - 107) / 9

# var(3x) = 9 * var(x)
var_y = ((20/9)**2) * var_x

print(round(var_y, 1))
