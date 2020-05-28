def main():
    print("main")
    nmax = 10
    rsum = ReimannSum(0, pi, nmax, func)
    print(rsum)
    n = 0
    R = 0
    for p in range (50, 200+1):
        n = num(p)
        R = Rev(n,p)
        print (p, n, R)

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

def num(p):
    return 1000 - (5*p)

def Rev(n,p):
    return n*p

def func(x):
    return sin(x)

def rfunc(f, x, dx):
    return f(x) * dx
