
### Yo!
'''
Another independent code-out of TTT. This time in the git repository. 
If you get to snag, work it out by error messages, testing and docs etc.
Avoid AI? We will for now. It might come in useful later though. 

*I surround myself with love*

Let's go! '''

#%%

# 1. display board function

def display_board(board): 

    print('|' + board[7] + '|' +  board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' +  board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' +  board[2] + '|' + board[3] + '|')

# 2. player input -> who's what marker, X or O?

def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose a marker X or O:  ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# 2. place marker function

def place_marker(board, marker, position):
    board[position] = marker


## Run test_board test 
  

test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
place_marker(test_board, 'X', 5)

display_board(test_board)

#%%

# 4. choose_first -> who goes first? 
import random
def choose_first(): 

    if random.randint(0,1) == 0:
        return 'P1'
    else: 
        return 'P2'

# 5. Win check -> is a diagnonal, row or column struck?

def win_check(board, mark): 

    return((board[1] == mark and board[2] == mark and board[3] == mark) or # rows
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)) 


# 6. Space_check -> is there a spare space? 

def space_check(board): 

    return board[position] == ''


# 7. Full_board_check = is the board full? If so, it's a draw

def full_board_check(): 

    space_check(board, i)



# 8. choose_position = what position do you choose? 
# def choose_positio():

#     position = 0

#     while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not in space_check(board): 
    

# 9. replay = play again? 





