#!/usr/bin/python
#filename Euler2.py

a1 = 1
print a1
a2 = 2
print a2
a3 = a1+a2
sum_even =2
while a3<=4000000:
    print a3
    if a3%2 ==0:
        sum_even += a3
        print 'even-valued', a3
    a1=a2
    a2=a3
    a3=a1+a2
print "sum=", sum_even
