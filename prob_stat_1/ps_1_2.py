import sys

def cnv(inp):
	ans=inp[0].split(',')
	print(ans)
	print(tuple(ans))	

cnv(sys.argv[1:])
