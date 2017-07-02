import sys
def accnt(trans):
	trans_type=trans[0::2]
	trans_amt=trans[1::2]
	amt=0
	cnt=0
	for x in trans_type:
		if x == 'D':
			amt=amt+int(trans_amt[cnt])
		if x == 'W':
			amt=amt-int(trans_amt[cnt])
		cnt=cnt+1
	print(amt)


accnt(sys.argv[1:])
