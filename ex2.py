a=float(input("valeurs de a: "))
b=float(input("valeurs de b: "))
if (a>0 and b<0) or (a<0 and b>0):
    print("le produit de a et b est negatif")
elif (a==0 or b==0):
    print("le produit de a et b est nul")
else:
    print("le produit de a et b est positif")