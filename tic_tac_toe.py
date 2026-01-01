import random

# ---------------- DISPLAY BOARD ----------------
def display_board(board):
    print('\n' * 50)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# ---------------- PLAYER INPUT ----------------
def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose X or O: ").upper()

    return ('X', 'O') if marker == 'X' else ('O', 'X')

# ---------------- PLACE MARKER ----------------
def place_marker(board, marker, position):
    board[position] = marker

# ---------------- WIN CHECK ----------------
def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )


# ---------------- GAME UTILITIES ----------------
def choose_first():
    return 'Player 1' if random.randint(0, 1) == 1 else 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position

def replay():
    return input("Play again? (Yes/No): ").lower().startswith('y')

# ---------------- MAIN GAME LOOP ----------------
print("Welcome to Tic Tac Toe!")

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    game_on = input("Ready to play? (Yes/No): ").lower().startswith('y')

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            pos = player_choice(board)
            place_marker(board, player1_marker, pos)

            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 wins!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("Draw!")
                break
            else:
                turn = 'Player 2'

        else:
            display_board(board)
            pos = player_choice(board)
            place_marker(board, player2_marker, pos)

            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 wins!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("Draw!")
                break
            else:
                turn = 'Player 1'

    if not replay():
        break
