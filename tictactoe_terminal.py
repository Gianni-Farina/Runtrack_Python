#Une liste contenant 9 fois "-".
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#Une variable pour définir le joueur , une pour définir un vainqueur
#et l'autre pour signaler que le jeu n'est pas fini. 
Player= "X"
Winner = None
gameRunning = True

#Création de la grille à l'aide de la liste.
def printGrid(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Création de la place des "pions" à l'aide de la liste.
def playerInput(board):
    number=int(input("Enter a number between 1 and 9: "))
    if number >= 1 and number <= 9 and board[number-1] == "-":
        board[number-1]=Player
    else:
        print("Chose another spot , a player is already in that spot!")

#On vérifie si les pions du joueur sont alignés horizontalement et si
#ils le sont on déclare le jouer à qui appartiennent les pions vainqueur.
def checkHorizontle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True

#On vérifie si les pions sont alignés verticalement et si ils le 
#sont on déclare le joueur à qui appartiennent les pions vainqueur.
def checkVertical(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return True

#On vérifie si les pions sont alignés en diagonale et si ils
#le sont on déclare le joueur possèdant les pions vainqueur.
def checkDiagonal(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return True

#On vérifie si il n'y a plus de "-" dans la grille et si c'est le cas on déclare
#une égalité, car si il n'y a pas de vainqueur et qu'il ne reste plus de place pour
#les pions, on ne peut plus continuer.
def checkDraw(board):
    global gameRunning
    if "-" not in board:
        printGrid(board)
        print("It's a draw!")
        gameRunning = False

#On vérifie les fonctions qui définissent une victoire et si c'est le cas
#on affiche le nom du vainqueur.
def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkVertical(board):
        print(f"The winner is {Winner} !")

#Une fonction permettant de changer le "X" en "O" à chaque coup.
def switchPlayer():
    global Player
    if Player == "X":
        Player = "O"
    else: 
        Player = "X"

#Une boucle qui effectue toutes ces fontions pendant que le jeu continue.
#Il n'y a pas de fin tant qu'il n'y a pas de vainqueur ou d'égalité.
while gameRunning:
    printGrid(board)
    playerInput(board)
    checkWin()
    checkDraw(board)
    switchPlayer()