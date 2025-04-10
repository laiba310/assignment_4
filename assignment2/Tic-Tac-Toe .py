import random

# Empty board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Win checker
def check_win(player):
    combos = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check for draw
def check_draw():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Choose position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Occupied! Try again.")
        except:
            print("Invalid! Try number 1-9.")

# Computer move
def computer_move():
    print("Computer is thinking...")
    available = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available)
    board[move] = "O"

# Main Game Loop
def play_game():
    print("Welcome to Tic Tac Toe (You vs Computer)")
    print("You are X, Computer is O")
    
    while True:
        print_board()
        player_move()

        if check_win("X"):
            print_board()
            print("🎉 You win!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        computer_move()

        if check_win("O"):
            print_board()
            print("💻 Computer wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

# Start the game
play_game()
