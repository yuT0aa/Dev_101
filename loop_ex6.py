"""
var n, max, pos : entier
debut
    max=0
    pos=0
    tanque 1:=1 alors
        lire n
        si n>max alors
            max:=n
            pos:=pos+1
        sinon si n=0 alors
            break    
        finsi
    fin tanque
    print(f"Le plus grand est {max}, position : {pos}")
fin    

"""

max=0
pos=0
while True:
    while True:
        n=input("Entrez un nombre : ")
        if n.isdigit()==True:
            break
    n=int(n)
    if n>max:
        max=n
        pos+=1
    elif n==0:
        break

print(f"Le plus grand est {max}, position : {pos}")

            