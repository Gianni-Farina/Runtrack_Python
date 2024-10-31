alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

#n=26 pour le nombre de lettre dans l'alphabet
n = 26

for i in range(1, n + 1):
    print(alphabet[:i])
    #i=1 donc (alphabet[:i]) c'est caractère par caractère
    #qui compose alphabet.