#!/usr/bin/python
# Filename: Euler10.py

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
from myUtil import isPrime

def test():
    sum=2
    print '2,'
    num=3
    while num<2000000:
        if not isPrime(num):
            num+=2
            continue
        #print num
        sum+=num
        num+=2
    print 'sum=',sum

if __name__=='__main__':
    from timeit import Timer
    t = Timer("test2()", "from __main__ import test2")
    print t.timeit(1)
 
# result: sum= 142913828922
