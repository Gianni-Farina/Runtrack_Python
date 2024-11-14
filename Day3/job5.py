def nombre_premier(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

k=2
while k<1001:
    if nombre_premier(k):
        print(k)
    k+=1