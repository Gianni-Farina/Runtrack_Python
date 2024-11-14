def triangle(a,b,c):
    return a+b>c and b+c>a and a+c>b

def type_triangle(a,b,c):
    if a==b==c:
        return "équilatéral"
    elif a==b or b==c or a==c:
        return "isocèle"
    else:
        return "simple"

def triangle_rectangle(a,b,c):
    if a > b and a > c :
        return a**2==b**2+c**2
    elif b > a and b > c :
        return b**2==a**2+c**2
    else:
        return c**2==b**2+a**2
    
a=int(input("Entrez la longueur de a :"))
b=int(input("\nEntrez la longueur de b :"))
c=int(input("\nEntrez la longueur de c :"))

if triangle(a,b,c):
    print("\nLe triangle peut être créer!")
    triangle_type=type_triangle(a,b,c)
    print("\nLe triangle est un triangle : ",triangle_type," !")
    if triangle_rectangle(a,b,c):
        print("\nLe triangle est aussi un rectangle.")
    else:
        print("\nLe triangle n'est pas rectangle.")