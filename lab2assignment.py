
import random

# Create an empty board
board = [" "] * 9

# Winning combinations
winning_positions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


# Display the game board
def display_board():
    print()

    for i in range(3):
        row = []

        for j in range(3):
            position = i * 3 + j

            if board[position] == " ":
                row.append(str(position + 1))
            else:
                row.append(board[position])

        print(" | ".join(row))

        if i < 2:
            print("--+---+--")

    print()


# Check whether a player has won
def check_winner(symbol):
    for line in winning_positions:
        if (board[line[0]] == symbol and
            board[line[1]] == symbol and
            board[line[2]] == symbol):
            return True

    return False


# Check whether the board is full
def check_draw():
    return " " not in board


# Get a valid move from the user
def user_move():
    while True:
        move = input("Enter a cell number (1-9): ")

        if not move.isdigit():
            print("Invalid input. Enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Enter a number between 1 and 9.")

        elif board[move - 1] != " ":
            print("This cell is already occupied.")

        else:
            board[move - 1] = "X"
            break


# Strategy 1: Random Move
def random_move():
    empty_cells = []

    for i in range(9):
        if board[i] == " ":
            empty_cells.append(i)

    if empty_cells:
        position = random.choice(empty_cells)
        board[position] = "O"


# Find a winning move for a symbol
def find_winning_move(symbol):
    for i in range(9):
        if board[i] == " ":
            board[i] = symbol

            if check_winner(symbol):
                board[i] = " "
                return i

            board[i] = " "

    return -1


# Strategy 2: Intelligent Move
def intelligent_move():

    # Try to win
    position = find_winning_move("O")

    if position != -1:
        board[position] = "O"
        return

    # Block the user's winning move
    position = find_winning_move("X")

    if position != -1:
        board[position] = "O"
        return

    # Choose the centre
    if board[4] == " ":
        board[4] = "O"
        return

    # Choose a corner
    corners = [0, 2, 6, 8]
    empty_corners = []

    for i in corners:
        if board[i] == " ":
            empty_corners.append(i)

    if empty_corners:
        position = random.choice(empty_corners)
        board[position] = "O"
        return

    # Choose a side
    sides = [1, 3, 5, 7]
    empty_sides = []

    for i in sides:
        if board[i] == " ":
            empty_sides.append(i)

    if empty_sides:
        position = random.choice(empty_sides)
        board[position] = "O"


# Main program
print("TIC-TAC-TOE GAME")
print("1. Random Move Strategy")
print("2. Intelligent Move Strategy")

while True:
    strategy = input("Choose strategy (1 or 2): ")

    if strategy == "1" or strategy == "2":
        break

    print("Invalid choice. Try again.")

# Play the game
while True:
    display_board()

    # Human player's turn
    print("Your turn (X)")
    user_move()

    if check_winner("X"):
        display_board()
        print("Congratulations! You win!")
        break

    if check_draw():
        display_board()
        print("The game is a draw!")
        break

    # Computer's turn
    if strategy == "1":
        random_move()
    else:
        intelligent_move()

    print("Computer's turn (O)")

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if check_draw():
        display_board()
        print("The game is a draw!")
        break