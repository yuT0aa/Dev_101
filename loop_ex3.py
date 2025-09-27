"""
var n, f: entier
debut
    lire n
    f:=0
    pour i allant de 0:n :
        f:=f*i
    fin pour
fin             
"""
n,f=int(input("n: ")),int()
f=1
for i in range(1,n+1):
    f*=i
print(f"{n}!={f}")
