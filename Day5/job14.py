def my_long_word(l,phrase):
    return phrase[l:]
phrase="Religion,idéologie,ressources,terre,méchanceté,amour ou simplement parce que peu importe à quel point la raison est pathétique, c'est suffisant pour déclencher une guerre. "
l=int(input("Choisi un nombre de caractère à enlever:"))
discour=my_long_word(l,phrase)
print("\n",discour)