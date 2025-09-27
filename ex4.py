"""
var a,b,c,x1,x2,delta=réel
debut
    ecrire "donner une valeur de a: "
    lire(a)
    ecrire "donner une valeur de b: "
    lire(b)
    ecrire "donner une valeur de c: "
    lire(c)
    delta=b**2-4*a*c
    si a=0 alors
        ecrire "l'equation de 1ére degre"
    sinon si delta<0 alors
        ecrire "l'equation n'a pas de solutions"
    sinon si delta=0 alors
        x1=-b/(2*a)
        ecrire "l'equation a une seule solution: x= ",x1
    sinon
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        ecrire "la premiere solution de l'equation ax^2+bx+c=0 est: x1= ",x1
        ecrire "la deuxieme solution de l'equation ax^2+bx+c=0 est: x2= ",x2
    finsi
fin
"""
a=float(input("saisir valeur de a: "))
b=float(input("saisir valeur de b: "))
c=float(input("saisir valeur de c: "))
delta=b**2-4*a*c
if delta<0:
    print("l'equation n'a pas de solution")
elif delta==0:
    x1=-b/(2*a)
    print("l'equation a une seule solution: x= ",x1)
else:
    x1=(-b+delta**(0.5))/(2*a)
    x2=(-b-delta**(0.5))/(2*a)
    print("la premiere solution de l'equation ax^2+bx+c=0 est: x1= ",x1)
    print("la deuxieme solution de l'equation ax^2+bx+c=0 est: x2= ",x2)