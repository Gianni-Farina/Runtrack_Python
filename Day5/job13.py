L=[10,20,30,20,10,50,60,40,80,50,40,None]
print(f"Voici la liste: {L[:-1]}")
L_sans_double=[]

i=0
while True:
    double=False
    k=0
    while True:
        if L[k] is None:
            break
        if L[i]==L[k]:
            if i!=k:
                double=True
        k+=1
    if not double :
        L_sans_double.append(L[i])
    i+=1
    if L[i] is None:
        break

print(f"Voici la liste sans doublons: {L_sans_double}")