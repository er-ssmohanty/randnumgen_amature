#! /usr/bin/python3
import numpy as np

x=float(input("Enter any real rational number: "))
howmany=int(input("Enter number of iterations: "))

cnt=0
next_var=x
maxval=1000

pool_total=np.zeros(maxval)

while cnt<howmany:
	cnt+=1
	next_var=((((next_var+1)**0.5)*((next_var-1)**0.5)/(next_var**0.5))*maxval)%maxval
	print(int(next_var))
	pool_total[int(next_var)]+=1

for i in range(len(pool_total)):
	if pool_total[i]>1:
		print("{}: {}".format(i,pool_total[i]))
