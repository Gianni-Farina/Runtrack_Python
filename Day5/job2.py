def les_fruits():
    fruit=["pomme","cerise","orange"]
    while True:
        le_fruit=input("Vous voulez quel fruit?")
        if le_fruit in fruit:
            print(f"\nTenez votre {le_fruit} !")
            break
        else:
            print("Désolé nous n'avons pas le fruit que vous voulez.")

les_fruits()