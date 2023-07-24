""" Tic Tac Toe in Python (no GUI) """

from random import randint as rint
from random import choice as rch

# ________________________ # Game Logic # __________________________ #


def displayBoard(b):

    # Displays the Board ...
    print()
    print(f" {b[1]} | {b[2]} | {b[3]} ".center(22, ' '))
    print(f"{'-'*3}+{'-'*3}+{'-'*3}".center(22, ' '))
    print(f" {b[4]} | {b[5]} | {b[6]} ".center(22, ' '))
    print(f"{'-'*3}+{'-'*3}+{'-'*3}".center(22, ' '))
    print(f" {b[7]} | {b[8]} | {b[9]} ".center(22, ' '))


def playerComputerLetters():

    # Players choosing their letter ...
    p, c = '', ''

    try:
        p = input("\nChoose your letter (x/o) : ").lower()
        if p not in ['x', 'o']:
            raise ValueError("\nInvalid Input!\n")
    except ValueError as e:
        while p not in ['x', 'o']:
            print(e)
            p = input("Choose your letter (x/o) : ").lower()

    if p == 'x':
        c = 'o'
    else:
        c = 'x'

    # Returns a tuple, that gets unpacked in Driver section
    return p.upper(), c.upper()


def possibleMoves(b, l):

    # List of possible moves ...
    pMoves = []

    # Finding the available positions ...
    for i in l:
        if b[i] == ' ':
            pMoves.append(i)

    # Return any random position from the set of possible moves ...
    if len(pMoves) != 0:
        return rch(pMoves)
    else:
        return -1

# __________________________________________________________________ #


# ________________________ # Result Logic # ________________________ #

def checkWin(b, letter):

    l = letter.upper()

    return (
        (b[1] == l and b[2] == l and b[3] == l) or

        (b[4] == l and b[5] == l and b[6] == l) or

        (b[7] == l and b[8] == l and b[9] == l) or

        (b[1] == l and b[4] == l and b[7] == l) or

        (b[2] == l and b[5] == l and b[8] == l) or

        (b[3] == l and b[6] == l and b[9] == l) or

        (b[1] == l and b[5] == l and b[9] == l) or

        (b[3] == l and b[5] == l and b[7] == l)
    )


def checkDraw(b):
    for i in range(1, 10):
        if b[i] != ' ':
            return False
    return True

# __________________________________________________________________ #


# _______________________ # Result Messages # ______________________ #

def winMessage():
    print('_'*23)
    print("\n", "You win. 😁".center(22, " "))
    print('_'*23)


def drawMessage():
    print('_'*23)
    print("\n", "It's a draw. 😐".center(22, " "))
    print('_'*23)


def lossMessage():
    print('_'*23)
    print("\n", "You lose. 😢".center(22, " "))
    print('_'*23)

# __________________________________________________________________ #


# ________________________ # Player Logic # ________________________ #

def getPlayerMove(b):

    # Querying the player for a valid position ...
    m = ''
    while m not in '1 2 3 4 5 6 7 8 9'.split(' ') \
            or not (b[int(m)] == ' '):
        m = input("\nEnter your position (1-9) : ")

    return int(m)

# __________________________________________________________________ #


# _______________________ # Computer Logic # _______________________ #

def getComputerMove(b, cl):

    if cl == 'x':
        pl = 'o'
    else:
        pl = 'o'

    # Check for the Computer's Winning Move ...
    for i in range(1, 10):
        # A copy of the Board to check for winning moves ...
        bc = b.copy()
        if bc[i] == ' ':
            bc[i] = cl.upper()
            if checkWin(bc, cl):  # DEFEAT the Player
                return i

    # Check for the Player's Winning Move ...
    for i in range(1, 10):
        # A copy of the Board to check for winning moves ...
        bc = b.copy()
        if bc[i] == ' ':
            bc[i] = pl.upper()
            if checkWin(bc, pl):  # BLOCK the Player
                return i

    # If no winning moves are available to either of them...

    # Check for any possible moves in the CORNERS...
    move = possibleMoves(b, [1, 3, 7, 9])
    if move:
        return move

    # Check for a possible move to the MIDDLE ...
    elif b[5] == ' ':
        return 5

    # Check for any possible moves in the SIDES...
    else:
        return possibleMoves(b, [2, 4, 6, 8])

# __________________________________________________________________ #


# ________________________ # Driver Code # _________________________ #

if __name__ == "__main__":

    plays = 0
    score = [0, 0, 0]

    # Display the Board ...
    print("\n T I C  T A C  T O E ".center(33, ' '))
    board = {1: "1", 2: "2", 3: "3", 4: "4",
             5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    displayBoard(board)

    # Start the game ...
    game = True

    while (game):

        plays += 1

        # Clear the Board
        for x in board.keys():
            board[x] = ' '

        # Player and Computer letters ...
        pl, cl = playerComputerLetters()

        # Who goes first? 1 -> Player, 0 -> Computer
        turn = rint(0, 1)

        # Run the game ...
        gameRunning = True

        while (gameRunning):

            # Player's turn ...
            if turn == 1:
                print("\n\nYour turn ...")
                displayBoard(board)
                move = getPlayerMove(board)
                board[move] = pl.upper()

                if checkWin(board, pl):
                    score[0] += 1
                    displayBoard(board)
                    winMessage()
                    gameRunning = False

                else:
                    if checkDraw(board):
                        score[1] += 1
                        drawMessage()
                        gameRunning = False

                    else:
                        turn = 1 - turn

            # Computer's turn ...
            else:
                print("\n\nComputer's turn ...")
                move = getComputerMove(board, cl)
                if move != -1:
                    board[move] = cl.upper()
                displayBoard(board)

                if checkWin(board, cl):
                    score[2] += 1
                    lossMessage()
                    gameRunning = False

                else:
                    if checkDraw(board):
                        score[1] += 1
                        drawMessage()
                        gameRunning = False

                    else:
                        turn = 1 - turn

        # Quit or New Game ...
        game = True if input(
            "\nDo you want to play again? (y/n) : ").lower() == 'y' \
            else False

    print(
        f"\n\n{'S C O R E'.center(33, ' ')}\n{'-'*33}\n{f'Plays = {plays}'.center(33, ' ')}\n\n Wins = {score[0]}  Draws = {score[1]}  Losses = {score[2]}\n{'-'*33}\n")
