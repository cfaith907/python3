#------Global vars-----

# Game board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9",]

#def game_still_going
game_still_going = True

# who won or tie
winner = None

# Whos Turn
current_player = "X"

#Display
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# display_board()

#play a game of tic tac toe
def play_game():

    # Display board
    display_board()

    #while game is running
    while game_still_going:
        
        #handle single turn of each player
        handle_turn(current_player)

        #check if game ended
        check_if_game_over()

        # swap between x and o
        flip_player()
    #game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#handle turn
#how does this work calling current_player as "player"?
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9: ")
    
    valid = False
    while not valid:


        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1 to 9: ")
   
        position = int(position) - 1 

        if board[position] =='-':
            valid = True
        else:
            print("you cant play there, already chosen, Try again. ")
    
    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

# check for 3 in row
def check_for_winner():

    #pull from a global value, this is require to modify.
    global winner

    #rows
    row_winner = check_rows()
    #column
    column_winner = check_columns()
    #diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #winner = None
        winner = None
    return


def check_rows():
    #set up global pull
    global game_still_going
    #check if rows have all same value and not -
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row is matched, trigger win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return winning char x or o
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    #set up global pull
    global game_still_going
    #check if rows have all same value and not -
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any column is matched, trigger win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return winning char x or o
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[1]

    return

def check_diagonals():
        #set up global pull
    global game_still_going
    #check if rows have all same value and not -
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #if any column is matched, trigger win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return winning char x or o
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
   
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    

    return

def flip_player():
    # globak var
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"
    
    return



play_game()
#
#board
#display board
#func start game
#alternate turns w/ x and o
#func chec win
    #check rows
    #check solumns 
    #check diaganols
#func chec tie
#flip between players

