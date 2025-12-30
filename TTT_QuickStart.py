
### Quick Start game - no 'ready to play' option
# SKIP TO LINE 90 FOR GAME LOOP


 # Creating function for board

import os

def display_board(board):
    
    os.system('cls')
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    

# What marker is Player 1?
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    

# Where do you place your marker? 
def place_marker(board, marker, position):
    board[position] = marker


# Who goes first? 
import random 

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

# Is there a win? 
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Is there a free space?
def space_check(board, position):
    
    return board[position] == ' '

# Is the board full? 
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Player chooses position
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# Play again? 
def replay():
    
    return input('Do you want to play again? Enter Yes or No (y or n)? : ').lower().startswith('y')



# Full game

print('Welcome to Tic Tac Toe!')

while True:
    
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    # print(turn + ' will go first.')

    
    game_on = True

    while game_on:

        if turn == 'Player 1':
            # Player1's turn.
            print(turn + ' will go first.')
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print(turn + ' will go first.')

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break