
def test_case():
	from numpy import sqrt
	from mysqrt import sqrt2
	
	xvalues=[0,2,1000,100,0.0001,1e8]
	small=1.0e-14
	for x in xvalues:
		s0=sqrt2(x,False)
		s_numpy=sqrt(x)
		print(f"for x={x}, s={s0}and snumpy={s_numpy}")   
		assert(s0-s_numpy)<small,f"square root disagreeswith numpy square root for x={x}"
