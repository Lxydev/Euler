#!/usr/bin/python
#Filename: Euler19.py

'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import string

mon = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    if year%400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def Euler19():
	print 'hello'
        sum=0
        start = 2 # 1900 is not a leap year. 1901/1/1 is a Tue
        for year in range(1901,2001):
            for month in range (1,13):
                if start %7 == 0:
                    sum +=1
                    print 'Sunday in', year, month
                if month ==2 and isLeapYear(year):
                    start +=1
                start = (start + mon[month-1]) % 7
        print 'sum=',sum            
            
if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler19()", "from __main__ import Euler19").timeit(1)
