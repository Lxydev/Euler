#!/usr/bin/python
#Euler_005.py

#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of 
#the numbers from 1 to 20?

from myUtil import isPrime

def getPrimeFactors(num):
	'''
	return the prime factors for a number. e.g: 
		input 10
		output: dict = { 2: 1, 5: 1}
	'''
	factors = {}
	prime = 2
	while num>1:
		while num % prime ==0:
			if prime in factors: 
				factors[prime] = factors[prime]+1
			else:
				factors[prime] = 1
			num = num / prime
		prime += 1
		while isPrime(prime) == False:
			prime +=1
		if prime > num:
			break; 
	#print factors
	return factors

primeFactors = {}

for i in range (2,21):
	tmp = getPrimeFactors (i)
	for a, b in tmp.items():
		if a in primeFactors:
			if primeFactors[a] < b: 
				primeFactors[a] = b
		else:
			primeFactors [a] = b

result = 1
for a, b in primeFactors.items():
	result *= a**b
print primeFactors, result
