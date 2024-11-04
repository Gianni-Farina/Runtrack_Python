def distance_parcourue(nombre_marches, hauteur_marche_cm):
    hauteur_totale_cm = nombre_marches * hauteur_marche_cm
    hauteur_totale_m = hauteur_totale_cm / 100
    
    distance_journaliere_m = 5 * (2 * hauteur_totale_m)
    distance_semaine_m = distance_journaliere_m * 7
    return distance_semaine_m

nombre_marches = int(input("Veuillez entrer le nombre de marches: "))
hauteur_marche_cm = float(input("Veuillez entrer la hauteur de chaque marche: "))

distance = distance_parcourue(nombre_marches, hauteur_marche_cm)
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance:.2f} m par semaine.")