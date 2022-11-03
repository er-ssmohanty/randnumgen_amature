#! /usr/bin/python3
def main():
    import numpy as np
    seed=float(input("Enter any real rational number: "))
    howmany=int(input("Enter number of iterations: "))
    randnum_list,pool_total=randnum_gen(seed,howmany)
    # for i in range(len(pool_total)):
	    # if pool_total[i]>1:
		    # print("{}: {}".format(i,pool_total[i]))

def randnum_gen(seed,maxcount,outputype="int",toprint=False):
    import numpy as np
    real_seed=(abs(seed**0.01)*1000000)%1000000
    cnt=0
    next_var=real_seed
    maxval=1000
    pool_list=[]
    pool_freq=np.zeros(maxval)

    while cnt<maxcount:
        cnt+=1
        next_var=(((((next_var+3.141592653589793)**2)+((next_var-3.141592653589793)\
            **2)+(next_var**2))/3)*maxval)%maxval
    if toprint:
        print(int(next_var))
    if outputype=="int":
        pool_list.append(int(next_var))
    else:
        pool_list.append(next_var)
    pool_freq[int(next_var)]+=1
    return pool_list, pool_freq

if __name__ == "__main__":
    main()
