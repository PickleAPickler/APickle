
'''
Ideas:

- Just have the GRID function with alan_grid passed in. Having the grid all set-up and ready to go? Don't have to put it in the main game code? 
- Just have player 1 = X    and   player 2 = O by default. Then have game code. 
- An alternative to the tuple unpacking in       which_symbol()    ? 

'''
# Creating function for grid
def GRID(grid):
    # clear_output()  
    
    print(grid[7] + grid[8]  + grid[9])
    print(grid[4] + grid[5]  + grid[6])
    print(grid[1] + grid[2]  + grid[3])
    

# What symbol is Player 1?
def which_symbol():
    symbol = ''
    
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('CUNT_1: Do you want to be X or O? ').upper()

    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    

# Where do you place your symbol? 
def place_symbol(grid, symbol, position):
    grid[position] = symbol


# Who goes first? 
import random 

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

# Is there a win? 
def win_check(grid,mark):
    
    return ((grid[7] == mark and grid[8] == mark and grid[9] == mark) or # across the top
    (grid[4] == mark and grid[5] == mark and grid[6] == mark) or # across the middle
    (grid[1] == mark and grid[2] == mark and grid[3] == mark) or # across the bottom
    (grid[7] == mark and grid[4] == mark and grid[1] == mark) or # down the middle
    (grid[8] == mark and grid[5] == mark and grid[2] == mark) or # down the middle
    (grid[9] == mark and grid[6] == mark and grid[3] == mark) or # down the right side
    (grid[7] == mark and grid[5] == mark and grid[3] == mark) or # diagonal
    (grid[9] == mark and grid[5] == mark and grid[1] == mark)) # diagonal

# Is there a free space?
def space_check(grid, position):
    
    return grid[position] == ' '

# Is the grid full? 
def full_grid_check(grid):
    for i in range(1,10):
        if space_check(grid, i):
            return False
    return True

# Player chooses position
def player_choice(grid):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9]  or not space_check(grid, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# Play again? 
def replay():
    
    return input('Do you want to play again? Enter Yes or No (y or n)? : ').lower().startswith('y')


# Full game

print('Welcome to Tic Tac Toe!')

while True:
    
    thegrid = [' '] * 10
    player1_symbol, player2_symbol = which_symbol()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            GRID(thegrid)
            position = player_choice(thegrid)
            place_symbol(thegrid, player1_symbol, position)

            if win_check(thegrid, player1_symbol):
                GRID(thegrid)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_grid_check(thegrid):
                    GRID(thegrid)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            GRID(thegrid)
            position = player_choice(thegrid)
            place_symbol(thegrid, player2_symbol, position)

            if win_check(thegrid, player2_symbol):
                GRID(thegrid)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_grid_check(thegrid):
                    GRID(thegrid)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


