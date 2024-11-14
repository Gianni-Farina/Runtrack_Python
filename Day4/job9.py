def moyenne(a,b,c):
    return (a+b+c)/3

a=int(input("Quelle note avez vous obtenu pour le premier examen?"))
b=int(input("\nPour le deuxième?"))
c=int(input("\nEt pour le troisième?"))

moyenne_étudiant=moyenne(a,b,c)

if moyenne_étudiant>15:
    print("\nTrès bon élève")
elif moyenne_étudiant>10:
    print("\nBon élève")
elif moyenne_étudiant>7:
    print("\nÉlève moyen")
elif moyenne_étudiant>0:
    print("\nÉlève devant faire des efforts")