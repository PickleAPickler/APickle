
### Yo!
'''
Another independent code-out of TTT. This time in the git repository. 
If you get to snag, work it out by error messages, testing and docs etc.
Avoid AI? We will for now. It might come in useful later though. 

*I surround myself with love*

Let's go! '''



# 1. DISPLAY BOARD

def display_board(board): 

    print('|' + board[7] + '|' +  board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' +  board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' +  board[2] + '|' + board[3] + '|')


## How to update game board? 
# https://www.youtube.com/watch?v=v4oW-yEffXs
# https://eitca.org/computer-programming/eitc-cp-ppf-python-programming-fundamentals/getting-started/lists-and-tic-tac-toe-game/examination-review-lists-and-tic-tac-toe-game/how-can-we-display-the-game-board-in-a-grid-like-format-using-a-for-loop-in-python/
# Peirian data? There was a solution there surely...

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

# region --> Run test_board test 
  

# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# place_marker(test_board, 'X', 5)

# display_board(test_board)
# endregion 

# 4. CHOOSE_FIRST -> WHO GOES FIRST? 
import random
def choose_first(): 

    if random.randint(0,1) == 0:
        return 'P1'
    else: 
        return 'P2'
    
# region --> choose_first test

#choose_first()
# endregion

# 5. WIN CHECK -> IS A DIAGNONAL, ROW OR COLUMN STRUCK?

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

# region win_check test
# wintest_board =  ['#','X','X','O',' ',' ',' ',' ',' ',' ']
# win_check(wintest_board, 'X')
# endregion 
# region win_check comments
# getting written fast? Duplicating the lines, indenting, dedenting, lining up.
# Any other games/programmes we could use this in?
# endregion
 

# 6. free_free_space_check -> is there a spare space? 

def free_space_check(board, position): 

    return board[position] == ' '

'''returns TRUE if there's space.  FALSE if board is full'''

# 7. FULL_BOARD_CHECK = is the board full? If so, it's a draw

def full_board_check(board): 
    for i in range (1,10): ### OHHHH. WHY CAN'T IT BE      1 - 10 ? RECREATE THIS ERROR AND USE PDB
        if free_space_check(board, i): # if free_space_check is True (there is a space), FBC returns false
            return False
    return True

# test_board = ['#','X',' ',' ',' ',' ',' ',' ',' ',' '] 
# full_board_check(test_board) 

     

# 8. CHOOSE_POSITION = what position do you choose? 
def choose_position(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not free_space_check(board, position):
        position = int(input('Choose a position (1 - 9):   '))

    return position

# region ALTERNATIVE? 
# How do we re-write the numberlist? Can we use range? 
'''
def choose_position(board):

    position = 0

    while position not in range (1 - 9) or not free_space_check(board, position):
        position = int(input('Choose a position (0 - 9):   '))

    return position
'''
# endregion


# 9. replay = play again? 

def replay():

    return input('Would you like to play again y or n?:   ').lower().startswith('y')

### GAME CODE 

print('Welcome to TTT!')

# import pdb; pdb.set_trace()  

''' pbd did not run with the script at first, but when isolated to jupyter window, it ran. 
Then, it ran without the jupyter window. Why didn't run before? '''

while True:

    alan_board = [' ']*10
    P1Marker, P2Marker, = player_input()
    turn = choose_first()
    print('You are' + turn + '.' + 'you will go first')

# region CHECK THIS OUT: https://realpython.com/python-while-loop/
# endregion 

 
     
    play_game = input('Are you ready to play?   ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    # else:
    #     game_on = False   ## Watch it! Why is this not necessary? 
        
    while game_on:
        if turn == 'P1':
            
            display_board(alan_board)
            position = choose_position(alan_board)
            place_marker(alan_board, P1Marker, position)

        

            if win_check(alan_board, P1Marker):
                display_board(alan_board)
                print('Well done! You won.')
                game_on = False

            else:
                if full_board_check(alan_board):
                    display_board(alan_board)
                    print(' The game is a draw! ')
                    break 
                else:
                    turn = 'P2'

        else:



            display_board(alan_board)
            position = choose_position(alan_board)
            place_marker(alan_board, P2Marker, position)

            if win_check(alan_board, P2Marker):
                display_board(alan_board)
                print('Well done! You won.')
                game_on = False

            else:
                if full_board_check(alan_board):
                    display_board(alan_board)
                    print(' The game is a draw! ')
                    break
                else:
                    turn = 'P1'
        
 
    if not replay():
        break

            




    







