EMPTY= " "
NUM_SQUARES = 9






def instruction ():
	print()
print("here are the intuctions: ")
instruction()


def ask_yes_no(question):
	"""Ask a yes or no question."""
	response = None
	while response not in ("y","n"):
		response = input (question).lower()
	return response
	
print(ask_yes_no("Yes or no?"))	

def new_board():
	"""Creates new game board"""
	board =[]
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board
	
def display_board(board):
	"""Displahy the game board on screen."""
	print("\n\t", board [0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board [3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board [6], "|", board[7], "|", board[8], "\n")

gameBoard = new_board()
display_board(gameBoard)