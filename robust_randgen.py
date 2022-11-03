#! /usr/bin/python3
import numpy as np

seed=float(input("Enter any real rational number: "))
howmany=int(input("Enter number of iterations: "))

real_seed=((seed**0.01)*1000000)%1000000
cnt=0
next_var=real_seed
maxval=1000

pool_total=np.zeros(maxval)

while cnt<howmany:
	cnt+=1
	next_var=(((((next_var+1)**2)+((next_var-1)**2)+(next_var**2))/3)*maxval)%maxval
	print(int(next_var))
	pool_total[int(next_var)]+=1

for i in range(len(pool_total)):
	if pool_total[i]>1:
		print("{}: {}".format(i,pool_total[i]))
