"""
var n,i,s: entier
debut
    lire n
    s:=1
    pour i allant de 2:n repeter
        si i%2:=0 alors
            s:=s+1/i
        sinon
            s:=s-1/i    
        fin si
    fin pour
    ecrire s
fin
"""
n=int(input("n: "))
s=1