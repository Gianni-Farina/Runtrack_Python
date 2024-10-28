initial = int(input("Combien avez vous de capital ?"))
rendement =int(input("Votre taux de rendement annuel est de combien ?"))

print("Votre capital est de",initial,"€\n")

gain = initial//100 *rendement
print(f"Le gain annuel de l'année 2024 est de {gain}€\n")

initial = initial + gain + 5000
rendement = rendement * 1.02
gain = initial//100 * rendement
print(f"Le gain annuel de l'année 2025 est de {gain}€\n")

initial = initial + gain * 0.90
rendement = rendement * 0.99
print(f"Votre nouveau solde d'insvestissement est de {initial}€")
gain = initial//100 * rendement

print(f"Vous avez gagné {gain}€.")