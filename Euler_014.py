#!/usr/bin/python
# -*- coding: cp936 -*-
#Filename: Euler14.py

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# to count the terms for number a
def countTerms(a):
    terms = 1
    while a!=1:
        if a%2 ==0:
            a/=2
        else:
            a=a*3+1
        terms +=1
    return terms
    
def euler14():
    limit = 1000000
    a=limit/2
    max_c = 0
    while a<limit:
        tmp = countTerms(a)
        if tmp>max_c:
            print "new high. number and terms = ", a, tmp
            max_c=tmp
        a+=1

if __name__=='__main__':
    from timeit import Timer
    print Timer("euler14()", "from __main__ import euler14").timeit(1)
