"""
var jour, mois, annee : Entier

Début
    Écrire("Donner le jour : ")
    Lire(jour)
    Écrire("Donner le mois : ")
    Lire(mois)
    Écrire("Donner l'année : ")
    Lire(annee)

    // Déterminer le nombre de jours dans le mois
    si mois=1 ou mois=3 ou mois=5 ou mois=7 ou mois=8 ou mois=10 ou mois=12 Alors
        nbJours ← 31
    Sinon si mois=4 ou mois=6 ou mois=9 ou mois=11 Alors
        nbJours ← 30
    Sinon
        nbJours ← 28
    FinSi

    // Calcul du lendemain
    Si jour < nbJours Alors
        jour ← jour + 1
    Sinon
        jour ← 1
        Si mois < 12 Alors
            mois ← mois + 1
        Sinon
            mois ← 1
            annee ← annee + 1
        FinSi
    FinSi

    Écrire("Le lendemain est : ", jour, "/", mois, "/", annee)
Fin
"""

jour=int(input("saisir le jour: "))
mois=int(input("saisir le mois: "))
annee=int(input("saisir l'annee: "))
if(mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
    nbJours=31
elif(mois==4 or mois==6 or mois==9 or mois==11):
    nbJours=30
else:
    nbJours=28
if(jour<nbJours+2):
    jour=jour+2
else:
    jour=1
    if(mois<12):
        mois==mois+1
    else:
        mois=1
        annee=annee+1
print("Le lendemain est: ",jour,"/",mois,"/",annee)