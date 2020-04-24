from math import *

def main():
    print("main")
    nmax = int(inf)
    rsum = ReimannSum(0, pi, nmax, func)
    print(rsum)

def func(x):
    return sin(x)

def rfunc(f, x, dx):
    return f(x) * dx

def ReimannSum(a, b, n, f):
    dx = (b - a)/n
    rsum = 0
    for i in range(1, n+1):
        rsum += f(a + i * dx) * dx
    return rsum

def summation(n0, n, f):
    sum = 0
    for i in range(n0,n+1):
        sum += f(i)
    return sum


main()
