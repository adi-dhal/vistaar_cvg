import sys
import numpy as np

def srt(inp):
	raw=inp[0].split(',')
	print(raw)
	for x in sorted(raw):
		print(x)

srt(sys.argv[1:])
