def dev(langage):
    if langage=="Python":
        print("\nTu es un développeur IA!")
    elif langage=="JavaScript":
        print("\nTu es un développeur web!")
    elif langage=="java":
        print("\nTu es un développeur logiciel!")
    elif langage=="reactjs":
        print("\nTu es un développeur mobile!")
    else:
        print("\nUn jour je serais le meilleur développeur...")
    
langage=input("Quel est votre langage informatique préféré?")
dev(langage)