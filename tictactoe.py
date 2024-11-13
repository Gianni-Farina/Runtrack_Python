BOARD = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

PLAYER1 = "X"
PLAYER2 = "O"
current_Player = PLAYER1
gameRunning = True

def printGrid(BOARD):
    print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
    print("----------")
    print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
    print("----------")
    print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])

def PlayerInput(BOARD, current_Player):
    while True:
        try:
            number = int(input(f"Player {current_Player}, enter a number between 1 and 9: "))
            if number >= 1 and number <= 9 and BOARD[number - 1] == "-":
                BOARD[number - 1] = current_Player
                return False
            else:
                print("Choose another spot, a player is already in that spot!")
        except ValueError:
            print("Please choose an integer between 1 and 9.")

def checkHorizontal(BOARD, current_Player):
    for row in range(0, 9, 3):
        if BOARD[row] == BOARD[row + 1] == BOARD[row + 2] == current_Player:
            return True
    return False

def checkVertical(BOARD, current_Player):
    for col in range(3):
        if BOARD[col] == current_Player and BOARD[col + 3] == current_Player and BOARD[col + 6] == current_Player:
            return True
    return False

def checkDiagonal(BOARD, current_Player):
    if BOARD[0] == BOARD[4] == BOARD[8] == current_Player:
        return True
    if BOARD[2] == BOARD[4] == BOARD[6] == current_Player:
        return True
    return False

def checkDraw(BOARD):
    if "-" not in BOARD:
        return True
    return False

def checkWin(BOARD, current_Player):
    if checkDiagonal(BOARD, current_Player) or checkHorizontal(BOARD, current_Player) or checkVertical(BOARD, current_Player):
        return True
    return False

def switchPlayer(current_Player):
    return PLAYER2 if current_Player == PLAYER1 else PLAYER1

def minimax(BOARD, depth, isMaximizingPlayer):
    if checkWin(BOARD, PLAYER2):
        return 1
    elif checkWin(BOARD, PLAYER1):
        return -1
    elif checkDraw(BOARD):
        return 0
    if isMaximizingPlayer:
        maxEval = float('-inf')
        for i in range(9):
            if BOARD[i] == "-":
                BOARD[i] = PLAYER2
                eval = minimax(BOARD, depth + 1, False)
                BOARD[i] = "-"
                maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for i in range(9):
            if BOARD[i] == "-":
                BOARD[i] = PLAYER1
                eval = minimax(BOARD, depth + 1, True)
                BOARD[i] = "-"
                minEval = min(minEval, eval)
        return minEval

def bestMove(BOARD):
    bestVal = float('-inf')
    bestMove = -1
    for i in range(9):
        if BOARD[i] == "-":
            BOARD[i] = PLAYER2
            moveVal = minimax(BOARD, 0, False)
            BOARD[i] = "-"
            if moveVal > bestVal:
                bestVal = moveVal
                bestMove = i
    return bestMove

def aiMove(BOARD):
    move = bestMove(BOARD)
    BOARD[move] = PLAYER2
    print(f"AI plays at position {move + 1}")

def select_mode():
    while True:
        mode = input("Single-player or multi-player? ").strip().lower()
        if mode in ["singleplayer", "single-player", "single"]:
            return mode
        elif mode in ["multiplayer", "multi-player", "multi"]:
            return mode
        else:
            print("Please enter only singleplayer or multiplayer!")

def multiplayer(BOARD, current_Player, gameRunning):
    while gameRunning:
        printGrid(BOARD)
        PlayerInput(BOARD, current_Player) 
        if checkWin(BOARD, current_Player):
            printGrid(BOARD)
            gameRunning = False
        elif checkDraw(BOARD):
            printGrid(BOARD)
            print("It's a draw!")
            gameRunning = False
        else:
            current_Player = switchPlayer(current_Player)

def singleplayer(BOARD, current_Player, gameRunning):
    while gameRunning:
        printGrid(BOARD)
        if current_Player == PLAYER1:
            PlayerInput(BOARD, current_Player)  # Passer current_Player ici
        else:
            aiMove(BOARD)
        if checkWin(BOARD, current_Player):
            printGrid(BOARD)
            gameRunning = False
        elif checkDraw(BOARD):
            printGrid(BOARD)
            print("It's a draw!")
            gameRunning = False
        else:
            current_Player = switchPlayer(current_Player)

def ask_to_play_again():
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "y"]:
                return True
            elif play_again in ["no", "n"]:
                print("Thank you for playing!")
                return False
            else:
                print("Please enter 'yes' or 'no'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def gameMode():
    while True:
        mode = select_mode()
        BOARD = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        current_Player = PLAYER1
        gameRunning = True
        if mode in ["singleplayer", "single", "single-player"]:
            print("You are playing as singleplayer.")
            singleplayer(BOARD, current_Player, gameRunning)
        elif mode in ["multiplayer", "multi", "multi-player"]:
            print("You are playing as multiplayer.")
            multiplayer(BOARD, current_Player, gameRunning)
        if not ask_to_play_again():
            break

if __name__ == "__main__":
    gameMode()