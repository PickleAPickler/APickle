

# 1. DISPLAY BOARD
import os 

def show_board(board): 
    os.system('cls')    
    
    print('|' + board[7] + '|' +  board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' +  board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' +  board[2] + '|' + board[3] + '|')


# 2. PLAYER INPUT -> WHOS WHAT MARKER, X OR O?

def player_input():

    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose a marker X or O:  ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# 3. PLACE MARKER FUNCTION

def place_marker(board, marker, position):
    board[position] = marker

 
# 4. CHOOSE_FIRST -> WHO GOES FIRST? 
import random
def choose_first(): 

    if random.randint(0,1) == 0:
        return 'P1'
    else: 
        return 'P2'
    

# 5. WIN CHECK -> IS A DIAGNONAL, ROW OR COLUMN COMPLETED?

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) 


# 6. free_free_space_check -> is there a spare space? 

def free_space_check(board, position): 

    return board[position] == ' '

'''returns TRUE if there's space.  FALSE if board is full'''


# 7. FULL_BOARD_CHECK = is the board full? If so, it's a draw

def full_board_check(board): 
    for i in range (1,10): 
        if free_space_check(board, i): 
            return False
    return True


# 8. CHOOSE_POSITION = what position do you choose? 
def choose_position(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not free_space_check(board, position):
        position = int(input('Choose a position (1 - 9):   '))

    return position


# 9. play_again = play again? 

def play_again():

    return input('Would you like to play again yes(y) or no(n)?:   ').lower().startswith('y')

### GAME CODE 

print('Welcome to Noughts and Crosses!')


while True:

    alan_board = [' ']*10
    P1Marker, P2Marker, = player_input()
    turn = choose_first()
    print('You are' + turn + '.' + 'you will go first')

    start_game = input('Are you ready to play?   ')
    
    if start_game.lower()[0] == 'y':
        game_on = True
    # else:
    #     game_on = False   ## Watch it! Why is this not necessary? 
        
    while game_on:
        if turn == 'P1':
            
            show_board(alan_board)
            position = choose_position(alan_board)
            place_marker(alan_board, P1Marker, position)
            
            if win_check(alan_board, P1Marker):
                show_board(alan_board)
                print('Well done! You won.')
                game_on = False

            else:
                if full_board_check(alan_board):
                    show_board(alan_board)
                    print(' The game is a draw! ')
                    break 
                else:
                    turn = 'P2'

        else:
            
            show_board(alan_board)
            position = choose_position(alan_board)
            place_marker(alan_board, P2Marker, position)

            if win_check(alan_board, P2Marker):
                show_board(alan_board)
                print('Well done! You won.')
                game_on = False

            else:
                if full_board_check(alan_board):
                    show_board(alan_board)
                    print(' The game is a draw! ')
                    break
                else:
                    turn = 'P1'
        
 
    if not play_again():
        break


