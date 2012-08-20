#!/usr/bin/python
#Filename: Euler17.py

import string

dict={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',\
	9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',\
	15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',\
	20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',\
	80:'Eighty',90:'Ninety',1000:'Onethousand'}

def digiLen(a):
	res=0
	if a<=20 or a==1000:
		res=len(dict[a]);
	elif a<100:
		if dict.has_key(a):
			#print dict[a],len(dict[a])
			res=len(dict[a])
		else:
			res=len(dict[int(a/10)*10])+len(dict[a%10])
	elif a%100==0:
		res=len(dict[a/100])+len('hundred')
	else:
		res=digiLen(int(a/100)*100)+len('and')+digiLen(a%100)
	return res
	
def Euler15():
	#print len('hundred')
	sum=0
	for i in range(1,1001):
		print i,digiLen(i)
		sum+=digiLen(i)
	print sum
	#print dict.has_key(102)
	#print dict.has_key(202)
	#dict[102]=32
	#print dict.has_key(102)

if __name__=='__main__':
    from timeit import Timer
    print Timer("Euler15()", "from __main__ import Euler15").timeit(1)
