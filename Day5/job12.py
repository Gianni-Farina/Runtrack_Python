L=[7,11,42,39,2,None]
print(f"Voici une liste: {L[:-1]}")
i=0
while True:
    min=i
    k=i+1
    while True:
        if L[k] is None:
            break
        if L[k]<L[min]:
            min=k
        k+=1
    L[i],L[min]=L[min],L[i]
    i+=1
    if L[i] is None:
        break

print(f"\nVoici la liste dans l'ordre croissant: {L[:-1]}")