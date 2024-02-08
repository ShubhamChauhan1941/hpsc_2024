x=int(input("enter number"))
s=2.0
kmax=10
for k in range (kmax):
	s=0.5*(s+(x/s))
	print(s)
	
