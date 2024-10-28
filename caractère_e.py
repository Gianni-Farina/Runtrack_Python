def lettre_e(phrase):
    return phrase.count("e")

phrase=input("Veuillez écrire votre phrase :")
nombre_de_e=lettre_e(phrase)
if lettre_e(phrase) :
    print(f"La phrase contient {nombre_de_e} fois lettre E !")
else :
    print("Il n'y a pas de lettre E dans votre phrase.\n")
    print(f"Et votre phrase est: {phrase}")