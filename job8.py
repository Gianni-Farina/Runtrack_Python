L = [8,24,27,48,2,16,9,7,84,91]
print("Voici une liste:")
print(L)
somme=sum(i for i in L if i%2==0)
print("Voici la somme des nombres pairs présents dans la liste:")
print(somme)