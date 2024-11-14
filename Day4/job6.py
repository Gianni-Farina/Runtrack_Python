def verif(nombre):
    if nombre>0:
        print(f"Le nombre est positif!\nVoici votre nombre: {nombre}.")
    else:
        print(f"Le nombre est négatif!\nVoici votre nombre: {nombre}.")

nombre=-5
while nombre<11:
    verif(nombre)
    nombre+=1