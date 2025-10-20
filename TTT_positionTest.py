
### * I surround myself with love* ###

# How can we get the marker glued to the board? 


def display_board(board): 

    print('|' + board[7] + '|' +  board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' +  board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' +  board[2] + '|' + board[3] + '|')

def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose a marker X or O:  ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def space_check(board, position): 
    return board[position] == ' '



def choose_position(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position (1 - 9):   '))

    return position

test_board = [' ']*10
display_board(test_board)
choose_position(test_board)



