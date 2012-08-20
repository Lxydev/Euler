#!/usr/bin/python

'''
assume f(n) = result
then: f(n+1) = f(n) + n(n+1)(n+1)
'''
sum = 4
for i in range(2,100):
    sum += (1+i)*i*(i+1)
print 'sum=',sum
'''

        
