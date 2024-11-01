L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50, None]
print(f"Voici une liste: {L[:-1]}")

def arrondir(nombre):
    entier = int(nombre)
    décimal = nombre - entier

    if décimal >= 0.5:
        return entier + 1
    else:
        return entier

L_entier = []

i = 0
while True:
    if L[i] is None:
        break
    L_entier.append(arrondir(L[i]))
    i += 1

for j in range(len(L_entier) - 1):
    for k in range(len(L_entier) - 1 - j):
        if L_entier[k] > L_entier[k + 1]:
            L_entier[k], L_entier[k + 1] = L_entier[k + 1], L_entier[k]

print(f"\nListe arrondie et triée dans l'ordre croissant :{L_entier}")