#!/usr/bin/python
#Filename: Euler23.py

import math

def isAbundant(n):
    if n<12:
        return False
    sum = 1
    for i in range (2,int(math.sqrt(n))+1):
        if n % i == 0:
            sum += i + n/i
            if i==n/i:
                sum -= i
    if sum>n:
        return True
    return False

def Euler23():
    dic = {12:True}
    for i in range (13,28124):
        if isAbundant(i):
            dic[i]=True
    
    total = 276 # 1+2+...+23
    for i in range (24,28124):
        result = False
        for j in range (12, int(i/2)+1):
            if dic.has_key(j) and dic.has_key(i-j):
                result = True
                break;
        if result==False:
            total += i
    print 'total = ', total

if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler23()", "from __main__ import Euler23").timeit(1)
