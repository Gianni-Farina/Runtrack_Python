def triangle(height):
    if height <= 0:
        print("Veuillez choisir une valeur positive.")
        return
    for i in range(height):
        espaces = ' ' * (height - i - 1)
        if i < height - 1:
            ligne = espaces + '/' + ' ' * (2 * i) + '\\'
        else:
            ligne = espaces + "/"+('_' * (2 * height -2))+"\\"
        print(ligne)

height = int(input("Choisis la hauteur de ton triangle: "))
triangle(height)