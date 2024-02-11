"""
Module for printing the square root of fuction by newton Raphson Method

"""

#this is the sqrt command
def sqrt2(x,debug):
	"""
	sqrt function 
	"""

	s=2.0
	kmax=100
	tolerance=1.0e-14 
	for k in range (kmax):
		k=k+1
		if debug:
			print(f"At iteration {k} the value is = {s:20.15f}")
		s0=s
		s=0.5*(s+(x/s))
		delta_s=s-s0
		if (abs(delta_s)/x<tolerance):
			break
	if debug:
		print(f"finally at iteration {k} the value is = {s:20.15f}")
	return s
