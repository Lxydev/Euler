#!/usr/bin/python
#Filename: Euler16.py

import string

def test():
    sum=0
    for n in str(2**1000): 
        sum+=int(n)
    print sum

if __name__=='__main__':
    from timeit import Timer
    print Timer("test()", "from __main__ import test").timeit(1)
