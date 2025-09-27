"""
var n, p:entier
debut
    lire n
    pour i allant de 1:10 :
        p:=n*i
        ecrire n,"*",i,"=",p
    fin pour
fin        
"""
n,p=int(input("valeur de n: ")),int()
for i in range(1,11):
    p=n*i
    print(f"{n}*{i}={p}")
    