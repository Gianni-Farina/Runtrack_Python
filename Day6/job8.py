def my_sort(lst):#création d'une fonction nommée my_sort avec comme paramètre lst pour liste.
    n = len(lst)#n pour compter la longueur de la liste.
    coups = 0#pour compter le nombre de coups pour avoir la liste triée.
    
    for i in range(n):#création d'une boucle qui va répéter élément de la liste.
        sorted_flag = True#une variable qui nous dis si la liste est triée , en l'occurence on part du principe que oui à chaque itération.
        for j in range(0, n - i - 1):#création d'une boucle pour éviter de comparer les mêmes éléments.
            if lst[j] > lst[j + 1]:#création d'une condition pour quand l'élément actuel est plus grand que le suivant.
                lst[j], lst[j + 1] = lst[j + 1], lst[j]#si c'est le cas , les éléments changent de place.
                coups += 1#on incrémente le compteur.
                sorted_flag = False#variable qui nous dis que la liste est pas encore triée
        if sorted_flag:#création d'une condition pour quand la liste est triée.
            break#on sort de la boucle si la liste est triée.
    print(f"Nombre total de coups nécessaires : {coups}")#on affiche le nombre de fois que la boucle a du s'effectuer pour triée la liste.
    return lst#la fonction renvoie la liste triée

liste = input("Entrez les nombres de la liste séparés par des espaces : ")#création d'une liste avec les nombres que l'on désire grâce à la commande input.
ma_liste = list(map(int, liste.split()))#variable contenant plusieurs fonctions: .split() pour utiliser les espaces comme séparateur, int pour convertir les chaînes de caractère en nombre entier, map pour que int s'applique à tout les entiers et list pour en faire une liste.
liste_triee = my_sort(ma_liste)#variable qui applique la fonction my_sort à la liste.

print("Liste triée :", liste_triee)#affichage de la liste.