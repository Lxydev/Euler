#!/usr/bin/python
#Filename: Euler15.py

import string

#100a+b
dict={101:2,202:6}

def f(a,b):
	if dict.has_key(100*a+b):
		print 'stored dic: f(%d,%d)=%d'%(a,b,dict[100*a+b])
		return dict[100*a+b]
	if a==0:
		dict[b]=1
		return 1
	if a==1:
		dict[100+b]=b+1
		print 'f(%d,%d)=%d'%(a,b,b+1)
		return b+1
	if a==b:
		print 'f(%d,%d)=f(%d,%d)*2'%(a,a,a-1,a)
		return f(a-1,b)*2
	print 'f(%d,%d) = f(%d,%d) + f(%d,%d)'%(a,b,a-1,b,a,b-1)
	dict[100*a+b]=f(a-1,b)+f(a,b-1)
	return f(a-1,b)+f(a,b-1)

def Euler15():
	print f(20,20)
	#print dict
	#print dict.has_key(102)
	#print dict.has_key(202)
	#dict[102]=32
	#print dict.has_key(102)

if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler15()", "from __main__ import Euler15").timeit(1)
