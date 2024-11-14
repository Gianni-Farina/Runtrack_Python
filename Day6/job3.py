def tapis(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            ligne = f"{i} +{'.' * n}+" 
        else:
            ligne = f"{i} |" 
            for j in range(n):
                if j == n - i:
                    ligne += " "
                else:
                    ligne += "#"
            ligne += "|"
        print(ligne)

n = int(input("Veuillez entrer la taille n: "))
tapis(n)
