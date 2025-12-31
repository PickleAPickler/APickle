
### COMPLETE THE ROW

# Testing the inserting of markers on the board. 
import os 


## Creating function for board



def display_board(board): 
   os.system('cls')
   
   # A single row of 2 spaces
   print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   print('-----------')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

   print(turn_message)




def turn_message(turn):
    os.system('cls')
    message = turn + ' will go first'

    return message


   
## Where do you place your marker? 
def place_marker(board, marker, position):
    board[position] = marker


## Player chooses a marker 


def player_input():

    marker = ' '

    while not (marker == 'O' or marker == 'X'):
        marker = input("Player 1: Please choose a marker 'X' or 'O':    ").upper()

    if marker == 'O':
        return ('O', 'X')
    else: 
        return ('X', 'O')
    
    

    
## Checking for spaces

def space_check(board, position):
    return board[position] == ' ' 

## Who's first? 

import random

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player_1'
    else:
        return 'Player_2'  

## Check for full board: 

def full_board_check(board):
    for i in range(1,7):
        if space_check(board, i):
            return False
    return True


## Player chooses position

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6] or not space_check(board, position): 
        position = int(input('Choose your next position (1-6):     '))
        
    return position

# Replay function

def replay():

   return input("Would you like to play again (y or n)?:    ").lower().startswith('y')


### GAME LOGIC

while True:
    
    alan_board = [' ']*7
    player1_marker,  player2_marker = player_input()
    turn = choose_first()
    # print(turn + ' will go first')
    


    game_on = True

    while game_on: 

        if turn == 'Player_1':

            display_board(alan_board)
            position = player_choice(alan_board)
            place_marker(alan_board, player1_marker, position)

            if full_board_check(alan_board):
                display_board(alan_board)
                print("We all win! The board is now full")
                game_on = False
            else:
                turn = 'Player_2'

        else:

            display_board(alan_board)
            position = player_choice(alan_board)
            place_marker(alan_board, player2_marker, position)

            if full_board_check(alan_board):
                display_board(alan_board)
                print("We all win! The board is now full")
                game_on = False
            else:
                turn = 'Player_1'

            

    if not replay():
        quit()



