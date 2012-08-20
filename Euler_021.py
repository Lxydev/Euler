#!/usr/bin/python
#Filename: Euler21.py

import math

def d(n):
    if n==1:
        return 0
    sum = 1
    for i in range (2,int(math.sqrt(n))):
        if n % i == 0:
            sum += i + n/i
    return sum

def Euler21():
    print 'hello'            
    sum=0
    for i in range (2,10000):
        a = d(i)
        if i==220:
            print '---220---',a,d(a)
        if i == d(a) and i!=a:
            print i,a
            sum += i
    print 'sum=',sum
                    
    
    
                   
if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler21()", "from __main__ import Euler21").timeit(1)
