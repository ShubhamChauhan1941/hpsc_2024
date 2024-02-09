def sqrt2(x):
	s=2.0
	kmax=100
	tolerance=1.0e-14 
	for k in range (kmax):
		k=k+1
		print(f"At iteration {k} the value is = {s:20.15f}")
		s0=s
		s=0.5*(s+(x/s))
		delta_s=s-s0
		if (abs(delta_s)/x<tolerance):
			break
	print(f"finally at iteration {k} the value is = {s:20.15f}")
