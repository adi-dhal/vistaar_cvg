ans=[]

for x in range(2001):
	if (x+1000) % 2 == 0:
		y=(x+1000)/10
		if y % 2 == 0:
			y=y/10
			if y % 2 == 0:
				y=y/10
				if y % 2 == 0:
					ans.append(int(x+1000))
print(ans)
