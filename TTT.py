from IPython.display import clear_output
import random
import os

# Creating an empty tic tac toe board
def display_board(board):
    clear_output()
    os.system('cls')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Choosing marker(X,O) -- Player input
def player_input():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player1, Choose 'X' or 'O': ").upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

# Placing the marker on board
def place_marker(board, marker, position):
    board[position] = marker

# Check for a win
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark)or
         (board[4] == mark and board[5] == mark and board[6] == mark)or
         (board[7] == mark and board[8] == mark and board[9] == mark)or
         (board[7] == mark and board[4] == mark and board[1] == mark)or
         (board[8] == mark and board[5] == mark and board[2] == mark)or
         (board[9] == mark and board[6] == mark and board[3] == mark)or
         (board[9] == mark and board[5] == mark and board[1] == mark)or
         (board[7] == mark and board[5] == mark and board[3] == mark))

# Random choice
def choose_first():
    i = random.randint(1,2)
    if i == 1:
        return "player1"
    else:
        return "player2"

# Space check at specified popsition
def space_check(board, position):
    
    return board[position] == ' '

# Checking full board (unoccupied)
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Player Input -- position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
    
    return position

# Play the game again?
def replay():
    
    r = int(input("Press 1: to play again\nPress 0: to quit\n"))
    if r == 0:
        return False
    else:
        return True

# Main Game
print('Welcome to Tic Tac Toe!')

while True:
    board = [" "]*10
    p1_marker,p2_marker = player_input()
    turn = choose_first()
    print(turn,"will go first")
    
    game_on = input("Ready to play? (y/n)")
    if game_on.lower() == "y":
        start = True
    else:
        start = False

    while start:
        #Player 1 Turn
        if turn == "player1":
            display_board(board)
            position = player_choice(board)
            place_marker(board,p1_marker,position)

            if win_check(board,p1_marker):
                display_board(board)
                print("** Player 1 has won! **")
                start = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("** Draw Game! **")
                    start = False
                else:
                    turn = "player2"
            # Player2's turn.
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,p2_marker,position)

            if win_check(board,p2_marker):
                display_board(board)
                print("** Player 2 has won! **")
                start = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("** Draw Game! **")
                    start = False
                else:
                    turn = "player1"
                #pass

    if not replay():
        break    