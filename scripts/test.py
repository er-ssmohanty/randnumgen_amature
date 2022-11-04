#! /usr/bin/python3
import robust_randgen as rr
rr.randnum_gen(100,10)
seeds=[92367628,45,0.0000341,0,-0.0000826,-88,-28787862]
for i in seeds:
	thelist,unnec=rr.randnum_gen(i,10)
	#print(thelist)
	#break
	with open("../results/{}_10_result.txt".format(i), "a") as f:
		#print(type(thelist))
		#break
		for s in thelist:
			f.write(str(s) +"\n")

