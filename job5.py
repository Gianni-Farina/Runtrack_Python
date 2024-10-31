def calcul(num1,operator,num2):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="/":
        print(num1//num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="%":
        print(num1%num2)

num1=int(input("Entrez un nombre :"))
operator=input("\nEntrez votre opérateur de calcul :")
num2=int(input("\nEntrez à nouveau un nombre :"))

calcul(num1,operator,num2)