def nombre_entier():
    while True:
        nombre=input("Veuillez entrer un nombre entier:")
        try:
            entier=int(nombre)
            if entier%2==0:
                print(f"\nLe nombre est pair: {entier}.")
            else:
                print(f"\nLe nombre est impair: {entier}.")

            return entier
        except ValueError:
            print("Il ne s'agit pas d'un nombre entier!\n")
        
nombre_entier()