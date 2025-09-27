"""
Écrire "Entrez un nombre de départ : "
Lire n

Pour i de 1 à 10 faire
    Écrire n + i
FinPour

"""
#methode 1 
n=int(input("n= "))
print(list(range(n+1,n+11)))


#methode 2
n=int(input("n= "))
for i in range(1,11):
    print(n+i)

    