#!/usr/bin/python
# Filename: Euler9.py

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

print 'hello Proj Euler 9!'

for a in range(198,333):
    start = a
    if a<500-a:
        start = 500-a
    for b in range (start,500):
        c=1000-a-b
        if c<b:
            break
        if a+b<=c:
            continue
        if a**2 + b**2 != c**2:
            print 'passed, ',a,b,c
            continue
        else:
            print'!--------------- a,b,c=',a,b,c
            print 'product of a,b,c = ',a*b*c
            quit()
