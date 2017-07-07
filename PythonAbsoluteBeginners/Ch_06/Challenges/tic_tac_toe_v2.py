"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: tic_tac_toe_v2.py
created on: 19 May, 2017
@author: Neil_Crerar

Chapter 6, Challenge 1
Improve the function aks_number() so that the function can be called within a
step value.  Make the default value of step 1.

NOTE: Got no idea why you would do this as it doesn't seem to fit any purpose 
within the context of the game?  Also can't seem to think how this is meant to
work as asking for a specific square on the grid to put your "X" into, not a 
selection of possible squares (unless that is the intention of course!)
"""

# Declare global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
    """Display game instructions"""
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    
    You will make your move by entering a number, 0-8.  The number
    will correspond to the board position as illustrated:
    
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
            
    Prepare yourself, human.  The ultimate battle is about to begin.\n
    """)


def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# MODIFIED: added a step value parameter with a default of 1
def ask_number(question, low, high, step=1):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high, step): 
        response = int(input(question))
    return response


def pieces():
    """Determine if the player of the computer goes first"""
    go_first = ask_yes_no("Do you require the first move (y/n)?: ")
    if go_first.lower() == "y":
        print("\nThen take the first move....... you need it")
        human = X 
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create a new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display the game board on-screen"""
    print("\n\t",board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t",board[3], "|", board[4], "|", board[5])
    print("\t", "---------")    
    print("\t",board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Creates a list of legal moves that can be played"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine if someone has won the game"""
    WAYS_TO_WIN = ((0, 1, 2)
                    ,(3, 4, 5)
                    ,(6, 7, 8)
                    ,(0, 3, 6)
                    ,(1, 4, 7)
                    ,(2, 5, 8)
                    ,(0, 4, 8)
                    ,(2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def human_move(board, human):
    """Get the human players move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
                
        # How would you apply the step value from 'ask_number' here in this
        # function?
                       
        move = ask_number("Where will you move? (0 - 8):", 0 , NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human.", end=" ")
            print("Choose another.\n")
    print("Fine...")
    return move


def computer_move(board, computer, human):
    """The computer makes it's move"""
    # Make a copy of the board to work with to decide on best move as need to
    # change it
    board = board[:]
    # the best board positions to have in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    # Loop through the legal moves trying the computers piece there looking
    # for a win
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # After checking a move, undo it
        board[move] = EMPTY
    # Loop through the legal moves seeing if there is a move where the human
    # can win
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # after checking a move, undo it
        board[move] = EMPTY
    # Since no-one wins on next move, select best square possible
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O 
    else:
        return X


def congratulate_winner(the_winner, computer, human):
    """Congratulate the winner of the game"""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!")
    
    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.\n" \
              "Proof that computers are superior to humans in all regards.")
    elif the_winner == human:
        print("No, no, no! It cannot be! Somehow you tricked me, human! \n" \
              "But never again.  I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
              "Celebrate today... for this is the best you will ever achieve.")
    
        
def main():
    display_instructions()
    computer, human = pieces()
    turn = X 
    board = new_board() 
    display_board(board) 
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human) 
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        
    the_winner = winner(board)
    congratulate_winner(the_winner, computer, human)

# Start the program
main()
input("\n\nPress the enter key to quit.")
