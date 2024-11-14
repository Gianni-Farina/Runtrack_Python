N=int(input("Veuillez choisir le nombre que vous voulez:"))
N=N+1

for i in range(1,N):
    print("-------------------------------")
    print("La table de multiplication de : ",i," est :\n" )
    for k in range(1,11):
        print(k," x ",i," = ",k*i)