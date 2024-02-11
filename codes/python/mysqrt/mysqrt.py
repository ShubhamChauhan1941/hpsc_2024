"""
Module for printing the square root of fuction by newton Raphson Method

"""

#this is the sqrt command
def sqrt2(x,debug):
	from numpy import nan
	"""
	sqrt function 
	"""
	if x==0:
		return 0
	elif x<0:
		return nan
		

	s=2.0
	kmax=100
	tolerance=1.0e-14 
	for k in range (kmax):
		k=k+1
		if debug:
			print(f"At iteration {k} the value is = {s:20.15f}")
		s0=s
		s= 0.5*(s+(x/s))
		#for cube root s=0.3333*((2*s)+(x/(s**2)))
		delta_s=s-s0
		if (abs(delta_s/x)<tolerance):
			break
	if debug:
		print(f"finally at iteration {k} the value is = {s:20.15f}")
	return s
