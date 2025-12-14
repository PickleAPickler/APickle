
## Display Board 'game': The board is displayed - that's the game! 
# 


def display_board(board):
   # clear_output()  
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def replay():
    
    return input('Do you want to play again? Enter Yes or No (y or n)? : ').lower().startswith('y')

# Game Logic 

print('Welcome to Display the Board game!')

while True:

    alan_board = [' ']*10
    play_game = input('Are you ready to play?   ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
          
    while game_on:
        display_board(alan_board)
        print('Nice, You displayed the board!')
        
        if not replay():
            quit()






