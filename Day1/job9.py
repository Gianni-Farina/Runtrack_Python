nom = "Clavier"
prix = 100
stock = 100

print("Produit:",nom)
print("Prix Unitaire :",prix,"€")
print("Quantité en stock:",stock,"\n")

achat=int(input("Combien voulez vous acheter de clavier?"))
if achat > stock :
     print("Il n'y a pas assez de stock!")
else :
     print("Vous avez acheter",achat,"claviers.")
     print("Il reste",stock,"claviers.\n")
     stock = stock - achat
     prix=prix*1.10
     print("Produit:",nom)
     print("Prix Unitaire:",prix,"€")
     print("Quantité en stock:",stock)