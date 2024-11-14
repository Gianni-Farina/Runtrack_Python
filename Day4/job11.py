def time_to_text():
    while True:
        temps=input("Combien de minutes?")
        try:
            nombre=int(temps)
            heure=nombre//60
            minute=int(nombre%60)
            print(f"\n{heure} heures et {minute} minutes")
            return nombre
        except ValueError:
            print("\nIl ne s'agit pas d'un nombre entier!")

time_to_text()