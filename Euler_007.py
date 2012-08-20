#!/usr/bin/python
# Filename: Euler7.py

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?


from myUtil import isPrime

count=1
num=3
print count,'2'
while True:
    while not isPrime(num):
        num+=2
    count+=1
    print count,num
    num+=2
    if count==10001:
        break
