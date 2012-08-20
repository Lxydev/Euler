#!/usr/bin/python
#Filename: Euler12.py

from myUtil import isPrime

primeList=[2]

# build a list of primes
def buildPrimeList():
    count=1
    num=3
    while True:
        while not isPrime(num):
            num+=2
        count+=1
        primeList.append(num)
        num+=2
        if count==2000:
            break

#input: a nature number
#output: the number of divisors
def countDivisors(a):
    result=1
    pos=0    
    divisor=primeList[pos]
    while divisor<=a:
        count=0
        #to find the next prime divisor
        while a%divisor==0:
            count+=1
            a /= divisor
        result *= count+1
        pos += 1
        if pos>=2000:
            print 'error'
            quit()
        divisor=primeList[pos]            
    return result

def euler12():
    no=1
    while True:
        num = no*(no+1)/2
        divisors = countDivisors(num)
        print no, num, divisors
        if divisors>500:
            break
        no +=1
    print 'final result is',num
    
if __name__=='__main__':
    from timeit import Timer
    t = Timer("buildPrimeList()", "from __main__ import buildPrimeList")
    print t.timeit(1)
    print Timer("euler12()", "from __main__ import euler12").timeit(1)
    #euler12()
    #print 'len',len(primeList)
    #print primeList
    #print 'divisors of 3', countDivisors(3)
    #print 'divisors of 21', countDivisors(21)
    #print 'divisors of 28', countDivisors(28)

    
