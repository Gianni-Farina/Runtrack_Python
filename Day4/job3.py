def add(a,b):
    print(a+b)

a=int(input("Veuillez choisir un nombre entier :"))
b=int(input("\nVeuillez choisir à nouveau un nombre entier :"))

if a+b < 100:
    print("Ton nombre est infèrieure à 100 :")
    add(a,b)
elif a+b < 1000:
    print("\nTon nombre est infèrieure à 1000 :")
    add(a,b)
else:
    print("\nTon nombre est supérieure à 1000 :")
    add(a,b)