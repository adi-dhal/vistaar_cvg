import sys
import math
	
def inp(arg):
	ans=[]
	for x in arg:
		ans.append(math.factorial(int(x)))
	print (ans)
	return
	
			
inp(sys.argv[1:])
