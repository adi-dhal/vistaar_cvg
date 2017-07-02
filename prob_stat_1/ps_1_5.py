import sys

def cal(n,ans):
	if(n == 1):
		x=1/ans
		return x
	else:
		x=n+float(float(n)/float(ans))
		return cal(n-1,x)
	
	
def inp(val):
	val=int(val[0])
	ans=val+1
	print(cal(val,val+1))
	ans=0
	for x in range(val):
		ans=float(x+1)/float(x+2)+ans
	print(ans)

inp(sys.argv[1:])
