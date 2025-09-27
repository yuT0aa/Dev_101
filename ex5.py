"""
var x,y,z,réel
debut
    ecrire "donner une valeur de x: "
    lire x
    ecrire "donner une valeur de y: "
    lire y
    ecrire "donner une valeur de z: "
    lire z
    si x>y et x>z alors
        ecrire "x est le plus grand"
        si z<y alors
            ecrire "x>y>z"
        sinon si y<z alors
            ecrire "x>z>y"
        finsi
    sinon si y>x et y>z alors
        ecrire "y est le plus grand"
        si x<z alors
            ecrire "y>z>x"
        sinon si z<x alors
            ecrire "y>x>z"
        finsi
    sinon
        ecrire "z est le plus grand"
        si x<y alors
            ecrire "z>y>x"
        sinon si y<x alors
            ecrire "z>x>y"
        finsi
    finsi
fin
"""
x=float(input("donner une valeur de x: "))
y=float(input("donner une valeur de y: "))
z=float(input("donner une valeur de z: "))
if x>y and x>z:
    print("x est le plus grand")
    if z<y:
        print("x>y>z")
    else:
        print("x>z>y")
elif y>x and y>z:
    print("y est le plus grand")
    if x<z:
        print("y>z>x")
    else:
        print("y>x>z")
else:
    print("z est le plus grand")
    if x<y:
        print("z>y>x")
    else:
        print("z>x>y")