#!/usr/bin/python
# -*- coding: cp936 -*-
# Filename: Euler4.py

#A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#assume the result looks like 9bccb9 = 9xy*9mn
#then y*n=9. 2 possibility as follows
#1) 9bccb9 = 9x1 * 9m9
#2) 9bccb9 = 9x3 * 9m3

# assume num is a 6 digit number
def isPalindromic(num):
    a = int(num/100000)
    if a!=num%10:
        return False
    num = (num-a*100001)/10
    a = int(num/1000)
    if a!= num%10:
        return False
    num = (num-a*1001)/10
    if num%11 !=0:
        return False
    return True

result = 0;
for i in range(9,-1,-1):
    for j in range (9,-1,-1):
        n1=900+i*10+3
        n2=900+j*10+3
        mul=n1*n2
        if isPalindromic(mul):
            print mul,'=',n1,'*',n2
            if mul>result:
                result=mul
        n1=900+i*10+1
        n2=900+j*10+9
        mul=n1*n2
        if isPalindromic(mul):
            print mul,'=',n1,'*',n2
            if mul>result:
                result=mul
print 'result=',result
#print 'is 143321 Palindromic?', isPalindromic(143321)
