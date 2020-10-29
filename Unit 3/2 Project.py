#!/usr/bin/env python
# coding: utf-8

# # Module 2 Required code  
#   
# 
# ## Note: Students of Dev330x on edX
# 
# > ### It is required to submit your required code for Module 2 within the edX course   
# > The completed code must be copied from the cell below and pasted in to the edX required code page at the end of Module 2 in the course "Introduction to Python: Creating Scalable, Robust, Interactive Code" on edX.  
# >  
# > **REQUIREMENTS**  
# > Submit all of the code in working order but you will only be graded on the the 2 functions below:
# - ### draw()  
#   - **use the following required keywords & functions:** `for`, `in`, `if`, `print`
# - ### mark()
#   - **use the following required keywords & functions:** `for`, `in`, `if`

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Required Code</B></font>   
# 
# 
# 
# ## Tic Tac Toe!   
# 
# ### Complete the Required Code in the Jupyter Notebook Required_Code_Mod02 and then paste into edX code submission page   
# 
# This is the same code assignment located as the project at the bottom of 3-2.5_Mod02_Practice.ipynb

# In[ ]:


# [ ] This project is an implementation a Tic Tac Toe game. 
# The logic of the game is in the `main` function, read it before writing any code.

# Use the description and examples under each of the following functions to implement them:
# 1) draw(board)
# 2) available(location, board)
# 3) mark(player, location, board)
# 4) check_win(board)
# 5) check_tie(board)

from IPython.display import clear_output #to clear the output (specific to Jupyter notebooks and ipython)
from random import randint

def draw(board):
    """
    Draw the `board` table.
    
    The board reflects the current state of the game, a number indicates an available location.
      
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        None
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 

         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X 
        -----------
         O | O | 6 
        -----------
         1 | X | 3 
    """
    #TODO
    pass
    
    
def available(location, board):
    """
    Check the availability of a `location` on the current `board`
    
    An available location on the board contains a number between 1 and 9 stored as a string.
    If the location contains 'X' or 'O', the location is not available and the function should return False;
    otherwise, the function should return True indicating the location is available
    
    args:
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game
    
    returns:
        True if the location is available. False if the location is not available
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 
         
         available("1", board) --> returns True
         available("9", board) --> returns True


         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X 
        -----------
         O | O | 6 
        -----------
         1 | X | 3 
        
         available("1", board) --> returns True, because there is a number
         available("5", board) --> returns False, because there is 'O'
         available("9", board) --> returns False, because there is 'X'
    """
    #TODO
    pass
    

def mark(player, location, board):
    """
    Mark `location` on the `board` with the `player` symbol.
    
    Should replace the `location` number on the board with `X` or `O`
    
    args:
        player: player's symbol, either 'X' or 'O'
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game
    
    returns:
        None
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 
         
         After mark('O', '4', board)
         The printout should look like:
         7 | 8 | 9 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | 3 
        
         After mark('X', '3', board)
         The printout should look like:
         7 | 8 | 9 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | X 
         
         After mark('O', '9', board)
         The printout should look like:
         7 | 8 | O 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | X 
    """
    #TODO
    pass
        
def check_win(board):
    """
    Check if there is a winner.
    
    A win happens if the either of the players was able to place 3 symbols ('X' or 'O') in:
    a horizontal, vertical, diagonal, or anti-diagonal placement.
    
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        True if there is a winner. False if there is no winner yet
        
    examples:
        Horizontal win:
        ================

         7 | O | 9 
        -----------
         X | X | X 
        -----------
         1 | O | 3 
        check_win(board) --> returns True, because 'X' won
        

         O | O | O 
        -----------
         X | X | 6 
        -----------
         X | O | 3 
        check_win(board) --> returns True, because 'O' won
    
    
        Vertical win:
        ================

         7 | 8 | X 
        -----------
         X | O | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'X' won
         

         X | O | O 
        -----------
         4 | O | 6 
        -----------
         X | O | X 
        check_win(board) --> returns True, because 'O' won
        
        
        Diagonal win:
        ================

         X | 8 | O 
        -----------
         4 | X | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'X' won
         

         O | X | O 
        -----------
         X | O | X 
        -----------
         1 | 2 | O 
        check_win(board) --> returns True, because 'O' won
        
        
        Anti-Diagonal win:
        ================

         O | 8 | X 
        -----------
         4 | X | X 
        -----------
         X | O | O 
        check_win(board) --> returns True, because 'X' won
         

         7 | 8 | O 
        -----------
         X | O | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'O' won
        
        
        No winners yet:
        ================

         O | 8 | 9 
        -----------
         4 | X | X 
        -----------
         X | O | O 
        check_win(board) --> returns False
    """
    #TODO
    pass

def check_tie(board):
    """
    Check the game for a tie, no available locations and no winners.
    
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        True if there is a tie. False the board is not full yet or there is a winner
        
    examples:

         O | O | X 
        -----------
         X | X | O 
        -----------
         O | O | X 
         
        check_tie(board) --> returns True
         


         O | O | 9 
        -----------
         X | X | 6 
        -----------
         X | O | 3 
         
        check_tie(board) --> returns False, because there are still available location
    """
    #TODO
    pass

def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 *'-' + "o")
    
def display(message):
    """
    Print `message` in the center of a 35 characters string
    
    args:
        message: string to display
    
    returns:
        None
    """
    print("|{:^35s}|".format(message))
    
def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while(not win and not tie):
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn] # contains 'X' or 'O'

        clear_output()
        
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)
        
        # check for win
        win = check_win(board)
        
        # check for tie
        tie = check_tie(board)
        

    # Display game over message after a win or a tie
    clear_output()
    
    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if(tie):
        display("Tie!")
    elif(win):
        display("Winner:")
        display(current_player)
    dashes()
  

# Run the game
main()

# --Completed--

from IPython.display import clear_output #to clear the output (specific to Jupyter notebooks and ipython)
from random import randint

def draw(board):
    """
    Draw the `board` table.
    
    The board reflects the current state of the game, a number indicates an available location.
      
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        None
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 

         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X 
        -----------
         O | O | 6 
        -----------
         1 | X | 3 
    """
    
    rows = 3
    cols = 3
    for row in range(rows):
        for col in range(cols):
            print("{:^3s}".format(board[row][col]), end = "")
            if(col <= 1):
                print("|", end = "")
        if(row <= 1):
            print()
            print(11 * '-')
    print()
    
    
def available(location, board):
    """
    Check the availability of a `location` on the current `board`
    
    An available location on the board contains a number between 1 and 9 stored as a string.
    If the location contains 'X' or 'O', the location is not available and the function should return False;
    otherwise, the function should return True indicating the location is available
    
    args:
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game
    
    returns:
        True if the location is available. False if the location is not available
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 
         
         available("1", board) --> returns True
         available("9", board) --> returns True


         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X 
        -----------
         O | O | 6 
        -----------
         1 | X | 3 
        
         available("1", board) --> returns True, because there is a number
         available("5", board) --> returns False, because there is 'O'
         available("9", board) --> returns False, because there is 'X'
    """
    
    if (location in "xXoO"):
        return False
    
    valid = False
    for row in board:
        if location in row:
            valid = True
            
    return valid

def mark(player, location, board):
    """
    Mark `location` on the `board` with the `player` symbol.
    
    Should replace the `location` number on the board with `X` or `O`
    
    args:
        player: player's symbol, either 'X' or 'O'
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game
    
    returns:
        None
        
    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9 
        -----------
         4 | 5 | 6 
        -----------
         1 | 2 | 3 
         
         After mark('O', '4', board)
         The printout should look like:
         7 | 8 | 9 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | 3 
        
         After mark('X', '3', board)
         The printout should look like:
         7 | 8 | 9 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | X 
         
         After mark('O', '9', board)
         The printout should look like:
         7 | 8 | O 
        -----------
         O | 5 | 6 
        -----------
         1 | 2 | X 
    """
    
    for row in board:
        if location in row:
            row[row.index(location)] = player 
        
def check_win(board):
    """
    Check if there is a winner.
    
    A win happens if the either of the players was able to place 3 symbols ('X' or 'O') in:
    a horizontal, vertical, diagonal, or anti-diagonal placement.
    
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        True if there is a winner. False if there is no winner yet
        
    examples:
        Horizontal win:
        ================

         7 | O | 9 
        -----------
         X | X | X 
        -----------
         1 | O | 3 
        check_win(board) --> returns True, because 'X' won
        

         O | O | O 
        -----------
         X | X | 6 
        -----------
         X | O | 3 
        check_win(board) --> returns True, because 'O' won
    
    
        Vertical win:
        ================

         7 | 8 | X 
        -----------
         X | O | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'X' won
         

         X | O | O 
        -----------
         4 | O | 6 
        -----------
         X | O | X 
        check_win(board) --> returns True, because 'O' won
        
        
        Diagonal win:
        ================

         X | 8 | O 
        -----------
         4 | X | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'X' won
         

         O | X | O 
        -----------
         X | O | X 
        -----------
         1 | 2 | O 
        check_win(board) --> returns True, because 'O' won
        
        
        Anti-Diagonal win:
        ================

         O | 8 | X 
        -----------
         4 | X | X 
        -----------
         X | O | O 
        check_win(board) --> returns True, because 'X' won
         

         7 | 8 | O 
        -----------
         X | O | X 
        -----------
         O | O | X 
        check_win(board) --> returns True, because 'O' won
        
        
        No winners yet:
        ================

         O | 8 | 9 
        -----------
         4 | X | X 
        -----------
         X | O | O 
        check_win(board) --> returns False
    """
    
    rows = 3
    cols = 3
    
    # Horizontal check
    for row in range(rows):
        if (board[row][0] == board[row][1] == board[row][2]):
            return True
    
    # Vertical check
    for col in range(cols):
        if (board[0][col] == board[1][col] == board[2][col]):
            return True 
    
    # Main-diagonal check
    if (board[0][0] == board[1][1] == board[2][2]):
        return True 
    
    # Anti-diagonal check
    if (board[0][2] == board[1][1] == board[2][0]):
        return True 
    
    # No winners yet
    return False

def check_tie(board):
    """
    Check the game for a tie, no available locations and no winners.
    
    args:
        board: 3x3 table (list of lists) containing the current state of the game
        
    returns:
        True if there is a tie. False the board is not full yet or there is a winner
        
    examples:

         O | O | X 
        -----------
         X | X | O 
        -----------
         O | O | X 
         
        check_tie(board) --> returns True
         


         O | O | 9 
        -----------
         X | X | 6 
        -----------
         X | O | 3 
         
        check_tie(board) --> returns False, because there are still available location
    """
    
    rows = 3
    cols = 3
    
    # No more selection options (full board)
    full_board = True
    for row in range(rows):
        for col in range(cols):
            if board[row][col] in "123456789":
                full_board = False
    
    # check for winners
    win = check_win(board)
    
    # Full board and no winner is a tie
    if(full_board and not win):
        return True
    else:
        return False

def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 *'-' + "o")
    
def display(message):
    """
    Print `message` in the center of a 35 characters string
    
    args:
        message: string to display
    
    returns:
        None
    """
    print("|{:^35s}|".format(message))
    
def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while(not win and not tie):
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn] # contains 'X' or 'O'

        clear_output()
        
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)
        
        # check for win
        win = check_win(board)
        
        # check for tie
        tie = check_tie(board)
        

    # Display game over message after a win or a tie
    clear_output()
    
    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if(tie):
        display("Tie!")
    elif(win):
        display("Winner:")
        display(current_player)
    dashes()
  

# Run the game
main()


# ### Test your code for the graded functions draw() & mark()
# Help ensure that required draw() & mark() functions will earn credit when submitted to edX by running the code below after the functions have been loaded in this notebook.
# 
# Be sure to meet the following **requirements** for draw() & mark() functions before submission to edX:  
# > 
# - ### draw()  
#   - **use the following required keywords & functions:** `for`, `in`, `if`, `print`
# - ### mark()
#   - **use the following required keywords & functions:** `for`, `in`, `if`

# In[ ]:


# Test your code for the graded functions draw() & mark()
# initializing game board
board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    
print("TEST 1\n")
draw(board)    
print("\nTest board above should look like below - Student should verify\n")
print("""7 | 8 | 9 
-----------
4 | 5 | 6 
-----------
1 | 2 | 3 """)

    
print("\n*******************************\nTEST 2\n")
mark("X", "7", board)
mark("O", "9", board)
mark("X", "5", board)
mark("O", "1", board)
mark("X", "3", board)

draw(board)

print("\nTest board above should look like below - Student should verify\n")
print(""" X | 8 | O 
-----------
 4 | X | 6 
-----------
 O | 2 | X""")

