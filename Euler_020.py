#!/usr/bin/python
#Filename: test.py

import string

def test():
    print 'hello'
    prod=1
    for n in range (2,100+1): 
        prod*=n
    sum=0
    for n in str(prod): 
        sum+=int(n)
    print sum

if __name__=='__main__':
    from timeit import Timer
    print Timer("test()", "from __main__ import test").timeit(1)
