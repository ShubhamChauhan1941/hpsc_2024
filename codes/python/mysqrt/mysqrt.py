x=float(input("enter value you want sqrt"))
s=2.0
kmax=10
for k in range (kmax):
    print(f"At iteration {k} the value is = {s}")
    s=0.5*(s+(x/s))
	
	
print(f"finally at iteration {k} the value is = {s}")
