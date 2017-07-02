import sys
import numpy as np

def det(inp):
	x=int(inp[0])
	y=int(inp[1])
	ans=np.zeros((x,y))
	for i in range(x):
		for j in range(y):
			ans[i,j]=i*j
	print(ans)

det(sys.argv[1:])
