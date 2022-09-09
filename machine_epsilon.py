import math
exp = abs(3.0*(4.0/3.0-1)-1)
def machine_epsilon():
    x = 1
    while (1 + x) != 1:
        y = x
        x /= 2
