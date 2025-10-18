

## Get user input for line 
### WHOOo! This cell works. Save as a test. 

# place_marker(theBoard, player1_marker, position)

marker = 'X'
alan_board = ['']*2 
position = int(input('Choose a position:   '))

def display_board(board):  
    print(board[1])

# Where do you place your marker? 
def place_marker(board, marker, position):
    board[position] = marker

place_marker(alan_board, 'X', position)

print(alan_board)