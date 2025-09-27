"""
var a,b,x=réel
debut
    ecrire "donner une valeur de a: "
    lire(a)
    ecrire "donner une valeur de b: "
    lire(b)
    ecrire "la solution de l'équation a*x+b=0 est: x=-b/a= ",x
fin    
"""
a,b=float(input("saisir valeur de a: ")),float(input("saisir valeur de b: "))
if (a==0):
    print("l'equation n'a pas de solution")
else:    
    x=-b/a
    print("la solution de l'equation a*x+b=0 est: x=-b/a= ",x)