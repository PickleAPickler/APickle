
# GOAL: Testing the     place_marker()    function. Can we input symbols onto the board? 
# UPDATE: We got the position input, Yay! Now we need to make the game so the line fills up  

## Creating function for board
def display_board(board):
     
   print('|' + board[1] + '|' + board[2] + '|')

## setting board as empty strings - these will be occupied by symbols. 

# alan_board = [' ']*3
# display_board(alan_board)

## Where do you place your marker? 
def place_marker(board, marker, position):
    board[position] = marker

## Checking for spaces

def space_check(board, position):
    return board[position] == ' '    

## Check for full board: 

def full_board_check(board):
    for i in range(1,3):
        if space_check(board, i):
            return False
    return True


## Player chooses position

def player_choice(board):
    position = 0
    
    while position not in [1,2,3] or not space_check(board, position): 
        position = int(input('Choose your next position (1-3):     '))
        
    return position

'''Let's insert a marker onto the board...'''

# alan_board = [' ']*3
# position = player_choice(alan_board)
# place_marker(alan_board, 'x', position)
# display_board(alan_board)

### Delving into game logic...

while True:
    
    alan_board = [' ']*3
    position = player_choice(alan_board)
    place_marker(alan_board, 'x', position)
    display_board(alan_board)

    # if full_board_check(alan_board):
    #     display_board(alan_board)
    #     print('The game is a draw!')
    # else:
    #     quit()
        
       




## Is there a space on the board? True if there is 

# def space_check(board, position):
#     return board[position] == ' '

'''

display_board(alan_board)
position = player_choice(alan_board)
place_marker(alan_board, test_marker, position)

'''














