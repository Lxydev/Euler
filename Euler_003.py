#!/usr/bin/python
# Filename: Euler3.py
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

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

num = 600851475143
max_p_factor = 3
a=max_p_factor+2

# to find the next prime factor
while True:
    #to find the next bigger prime number
    while not isPrime(a):
        if a>=num:
            break # found result: max_p_factor
        else:
            a+=2
    if a>=num:
        break # found result: max_p_factor
    elif num%a==0:
        max_p_factor=a
        num = num/a # a bug: need to loop here! 
        if a>=num:
            break
        print 'found one prime factor=',a
    else:
        print 'prime, but not factor', a
        a+=2
if a==num:
    max_p_factor=a
print 'final result is',max_p_factor

#print '600851475143 is prime?', isPrime(600851475143)
#print '23 is prime?', isPrime(23)
#print '34 is prime?', isPrime(34)
#print '95 is prime?', isPrime(95)
#print '79 is prime?', isPrime(79)


