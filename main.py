from math import *

def main():
    print("main")
    L = 0 #Limit
    a = 0
    print(func(-1))



    

def func(x):
    return (x+1)/(x*x-x-2)

def Limit(a):
    epsilon = 100
    delta = 100
    x = delta - a
    for i in range (1, 100):
        if (abs(x - a) > 0) and (abs(x - a) < delta):
            x = 1


main()
