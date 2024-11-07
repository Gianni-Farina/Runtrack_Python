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
SinglePlayer = None
MultiPlayer = None

def single():
    global SinglePlayer
    global MultiPlayer
    while True:
        AloneOrNot=input("Single-player or multi-player?").strip().lower()
        if AloneOrNot in ["singleplayer", "single-player", "single"]:
            SinglePlayer=True
            MultiPlayer=False
            break
        elif AloneOrNot in ["multiplayer", "multi-player", "multi"]:
            MultiPlayer=True
            SinglePlayer=False
            break
        else:
            print("Please enter only singleplayer or multiplayer!")
    if SinglePlayer:
        print("You are playing as  singleplayer.")
    elif MultiPlayer:
        print("You are playing as multiplayer.")
        


#Création de la grille à l'aide de la liste.
def printGrid(BOARD):
    print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
    print("----------")
    print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
    print("----------")
    print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])

#Fonction qui met à la place que l'on choisis les "pions" à l'aide de la liste.
#Qui permet aussi d'avoir uniquement les nombres entiers compris de 1 à 9.
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
            print("Please chose an integer number.")

#On vérifie si les pions du joueur sont alignés horizontalement et si
#ils le sont on déclare le joueur à qui appartiennent les pions vainqueur.
def checkHorizontle(BOARD):
    global current_Player
    global Winner
    for row in range(0, 9, 3):
        if BOARD[row] == BOARD[row + 1] == BOARD[row + 2] == current_Player:
            Winner = BOARD[row]
            return True

#On vérifie si les pions sont alignés verticalement et si ils le 
#sont on déclare le joueur à qui appartiennent les pions vainqueur.
def checkVertical(BOARD):
    global current_Player
    global Winner
    for col in range(3):
        if BOARD[col] == current_Player and BOARD[col+3] == current_Player and BOARD[col+6] == current_Player:
            Winner = BOARD[col]
            return True

#On vérifie si les pions sont alignés en diagonale et si ils
#le sont on déclare le joueur possèdant les pions vainqueur.
def checkDiagonal(BOARD):
    global Winner
    global current_Player
    if BOARD[0] == BOARD[4] == BOARD[8] or BOARD[2] == BOARD[4] == BOARD[6] == current_Player:
        Winner = BOARD[0]
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
    global gameRunning
    if checkDiagonal(BOARD) or checkHorizontle(BOARD) or checkVertical(BOARD):
        print(f"The winner is {Winner} !")
        printGrid(BOARD)
        gameRunning=False

#Une fonction permettant de changer le "X" en "O" à chaque coup.
def switchPlayer():
    global current_Player
    if current_Player == PLAYER1:
        current_Player = PLAYER2
    else: 
        current_Player = PLAYER1

#Une boucle qui effectue toutes ces fontions pendant que le jeu continue.
#Il n'y a pas de fin tant qu'il n'y a pas de vainqueur ou d'égalité.
while gameRunning:
    printGrid(BOARD)
    PlayerInput(BOARD)
    checkWin()
    checkDraw(BOARD)
    switchPlayer()