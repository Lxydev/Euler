#!/usr/bin/python
#Filename: Euler 22.py

import string

def Euler22():
    f = file('names.txt','r')
    namelist = sorted([ x.strip('"') for x in f.read().split(",")])
    f.close()
    total = 0
    for i in range(0,len(namelist)):
        total += sum(ord(c)-ord('A')+1 for c in namelist[i])*(i+1)
    print 'name score is', total
        
if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler22()", "from __main__ import Euler22").timeit(1)
