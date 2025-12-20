
### COMPLETE THE ROW

# Testing the inserting of markers on the board. 


## Creating function for board

import os 

def display_board(board): 
   os.system('os')
   
   # A single row of 2 spaces
   print('|' + board[1] + '|' + board[2] + '|')

   
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

# Replay function

def replay():

   return input("Would you like to play again (y or n)?:    ").lower().startswith('y')


### GAME LOGIC

while True:
    
    alan_board = [' ']*3
    marker = 'X'

    game_on = True

    while game_on: 

        display_board(alan_board)
        position = player_choice(alan_board)
        place_marker(alan_board, marker, position)

        if full_board_check(alan_board):
            display_board(alan_board)
            print('Nice, you completed the row!')
            game_on = False

            if not replay():
                quit()



