"""
var n, tot ,comp :entier
var moy :reel
Début
    tot:=0
    comp:=0
    n:=1

    Tant que n!=0 repeter
        ecrire "Entrez un nombre (0 pour arrêter) : "
        Lire n
        Si n!=0 Alors
            tot:=tot+n
            comp:=comp+1
        Finsi
    FinTantQue

    Si comp>0 alors
        moy:=tot/comp
        ecrire "La moyenne est ", moy
    Sinon
        ecrire "Aucun nombre saisi."
    FinSi
Fin
"""

tot=0
comp=0
while True:
    while True:
        n=input("Entrez un nombre n: ")
        if n.isdigit()==True:
            break
    n=int(n)
    if n!=0:
        tot+=n
        comp+=1
    else:
        break
if comp!=0:
    moy=tot/comp
    print(f"la moyenne est {moy}")
else:
    print("impossible de calculer la moyenne")