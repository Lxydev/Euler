#!/usr/bin/python
#filename Euler1.py

value_dividableBy3 = ( 3+ 999) * 333 / 2
print value_dividableBy3

value_dividableBy5 = (5+995)*199/2
print value_dividableBy5

value_dividableBy15 = (15+990)*66/2
print value_dividableBy15

value = value_dividableBy3 + value_dividableBy5 - value_dividableBy15
print 'the final result is', value
