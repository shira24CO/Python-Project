import math
import sympy as sp


def trapez(f,a,b,n):
    I = 0
    result = 0
    i = 0
    size = (b-a)/n
    while i < n:
        result += (1/2)*(size)*(f(a)+f(a+size))
        a +=size
        i +=1
    return result

def simpson(f,a,b,n):
    h = (b-a)/n
    result = f(a)+f(b)
    size = (b-a)/n
    i=0
    a+=size
    while i < (n - 1):
        if i % 2 == 0:
            result += 4 * f(a)
        else:
            result += 2 * f(a)
        a += size
        i += 1
    return result*(1/3)*h

f = lambda x:sp.sin(x)
print(trapez(f,0,math.pi,4))
print(simpson(f,0,math.pi,4))
