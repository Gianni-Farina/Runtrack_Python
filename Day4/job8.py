def primeur(type,saison):
    if type=="fruits" and saison=="été":
        print("Poire,Fraise,Cassis")
    elif type=="fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    elif type=="légumes" and saison=="été":
        print("artichaut, aubergine,navet")
    elif type=="légumes" and saison=="hiver":
        print("carotte, topinambour, endive")

type=input("Vous préfèrez les fruits ou les légumes?")
saison=input("\nVous préfèrez l'hiver ou l'été?")

primeur(type,saison)