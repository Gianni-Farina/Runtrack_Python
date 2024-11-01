L=[8,24,27,48,2,16,9,102,7,84,91]
print("Voici une liste:")
print(L)
somme=sum(i for i in L if i>24 and i<91)
print(f"\nVoici la somme des nombres de la liste compris entre 25 et 90: {somme}.")