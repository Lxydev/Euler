#!/usr/bin/python
# Filename: myUtil.py

import math

def isPrime(a):
    if a==2:
        return True
    if a%2==0:
        return False
    b=int(math.sqrt(a))
    if b%2==0:
        b-=1
    #print 'b=',b
    while b>1:
        if a%b ==0:
            return False
        b-=2
    return True


# End of myUtil.py