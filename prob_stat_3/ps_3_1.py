import numpy as np
from scipy import optimize
import sys

def f(val):
	return(2510*np.log(2800000.0/(2800000.0-13300.0*float(val))))-9.81*float(val)-335
def fd(val):
	return -2510*(((2800000.0-13300.0*float(val))*13300.0)/2800000.0)-9.81
def newton():
	return optimize.newton(f,70.0,fprime=fd,tol=0.00001)

def secant():
	return optimize.newton(f,10.0,tol=0.00001)

def bisection(l,h,tol):
	root = (l+h)/2.0
	while (h-l)/2.0 > tol:
		if f(root) == 0:
			return root
		elif f(l)*f(root) < 0:
			h = root
		else :
			l = root
		root = (l+h)/2.0
		
	return root

if(sys.argv[1] == "bisection"):
	print(bisection(0,100,0.00001))
if(sys.argv[1] =="newton"):
	print(newton())
if(sys.argv[1] =="secant"):
	print(secant())

