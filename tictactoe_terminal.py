#Une liste contenant 9 fois "-".
BOARD = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#Une variable pour définir le joueur , une pour définir un vainqueur
#et l'autre pour signaler que le jeu n'est pas fini. 
PLAYER1= "X"
PLAYER2= "O"
current_Player = PLAYER1
Winner = None
gameRunning = True

#Création de la grille à l'aide de la liste.
def printGrid(BOARD):
    print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
    print("----------")
    print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
    print("----------")
    print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])

#Fonction qui met à la place que l'on choisis les "pions" à l'aide de la liste.
#Qui permet aussi d'avoir uniquement des nombres entiers compris de 1 à 9.
def PlayerInput(BOARD):
    while True:
        try:
            number=int(input("Enter a number between 1 and 9: "))
            if number >= 1 and number <= 9 and BOARD[number-1] == "-":
                BOARD[number-1]=current_Player
                return False
            else:
                print("Chose another spot , a player is already in that spot!")
        except ValueError:
            print("Chose an integer number please!")

#On vérifie si les pions du joueur sont alignés horizontalement et si
#ils le sont on déclare le joueur à qui appartiennent les pions vainqueur.
def checkHorizontle(BOARD):
    global Winner
    if BOARD[0] == BOARD[1] == BOARD[2] and BOARD[0] != "-":
        Winner = BOARD[0]
        return True
    elif BOARD[3] == BOARD[4] == BOARD[5] and BOARD[3] != "-":
        Winner = BOARD[3]
        return True
    elif BOARD[6] == BOARD[7] == BOARD[8] and BOARD[6] != "-":
        Winner = BOARD[6]
        return True

#On vérifie si les pions sont alignés verticalement et si ils le 
#sont on déclare le joueur à qui appartiennent les pions vainqueur.
def checkVertical(BOARD):
    global Winner
    if BOARD[0] == BOARD[3] == BOARD[6] and BOARD[0] != "-":
        Winner = BOARD[0]
        return True
    elif BOARD[1] == BOARD[4] == BOARD[7] and BOARD[1] != "-":
        Winner = BOARD[1]
        return True
    elif BOARD[2] == BOARD[5] == BOARD[8] and BOARD[2] != "-":
        Winner = BOARD[2]
        return True

#On vérifie si les pions sont alignés en diagonale et si ils
#le sont on déclare le joueur possèdant les pions vainqueur.
def checkDiagonal(BOARD):
    global Winner
    if BOARD[0] == BOARD[4] == BOARD[8] and BOARD[0] != "-":
        Winner = BOARD[0]
        return True
    elif BOARD[2] == BOARD[4] == BOARD[6] and BOARD[2] != "-":
        Winner = BOARD[2]
        return True

#On vérifie si il n'y a plus de "-" dans la grille et si c'est le cas on déclare
#une égalité, car si il n'y a pas de vainqueur et qu'il ne reste plus de place pour
#les pions, on ne peut plus continuer.
def checkDraw(BOARD):
    global gameRunning
    if "-" not in BOARD:
        printGrid(BOARD)
        print("It's a draw!")
        gameRunning = False

#On vérifie les fonctions qui définissent une victoire et si c'est le cas
#on affiche le nom du vainqueur.
def checkWin():
    if checkDiagonal(BOARD) or checkHorizontle(BOARD) or checkVertical(BOARD):
        print(f"The winner is {Winner} !")

#Une fonction permettant de changer le "X" en "O" à chaque coup.
def switchPlayer():
    global current_Player
    if current_Player == PLAYER1:
        current_Player = PLAYER2
    else: 
        current_Player

#Une boucle qui effectue toutes ces fontions pendant que le jeu continue.
#Il n'y a pas de fin tant qu'il n'y a pas de vainqueur ou d'égalité.
while gameRunning:
    printGrid(BOARD)
    PlayerInput(BOARD)
    checkWin()
    checkDraw(BOARD)
    switchPlayer()