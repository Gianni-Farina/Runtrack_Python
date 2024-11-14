def chiffrer_cesar(message, decalage):
    resultat = ""
    for char in message:
        if char.isupper():
            resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        elif char.islower():
            resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        else:
            resultat += char
    return resultat

message = input("Veuillez entrer le message à chiffrer : ")
decalage = 3
message_chiffre = chiffrer_cesar(message, decalage)

print("Message chiffré :", message_chiffre)