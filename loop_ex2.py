"""
var n, s: entier
debut
    lire n
    s:=0
    pour i allant de 0:n :
        s:=s+i
    fin pour
fin             
"""
n,s=int(input()),int()
s=0
for i in range(1,n+1):
    s+=i
print(s)
