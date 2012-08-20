#!/usr/bin/python
#Filename: test.py

import string

def process(data):
	print 'hello'
	print data
	for i in range (len(data)-2,-1,-1):
		for j in range (0,i+1):
			if data[i+1][j] > data[i+1][j+1]:
				data[i][j] += data[i+1][j]
			else:
				data[i][j] += data[i+1][j+1]
	print data[0][0]			    
	#data[i][j]=999
	#print 'ln=%d,co=%d,data=%d',i+1,j+1,data[i][j]
	
	
def Euler18():
	f = file ('Euler_018data.txt', 'r')
	#f = file ('triangle.txt', 'r') # For Euler Problem 67
	tri = []
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		else:
			ln = [int(x) for x in line.split()]
			#print 'ln=',ln
			tri.append(ln)
	#print tri
	print 'length=',len(tri)
	f.close()
	process(tri)
	
if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler18()", "from __main__ import Euler18").timeit(1)
