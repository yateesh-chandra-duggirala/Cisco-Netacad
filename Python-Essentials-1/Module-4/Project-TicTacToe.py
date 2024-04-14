'''
Scenario:
Your task is to write a simple program which pretends to play tic-tac-toe with the user. 
To make it all easier for you, we've decided to simplify the game. 

Here are our assumptions:

- the computer (i.e., your program) should play the game using 'X's;
- the user (e.g., you) should play the game using 'O's;
- the first move belongs to the computer. it always puts its first 'X' in the middle of the board;
- all the squares are numbered row by row starting with 1 (see the example session below for reference)
- the user inputs their move by entering the number of the square they choose the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
-the program checks if the game is over. 
- there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
- the computer responds with its move and the check is repeated;
- don't implement any form of artificial intelligence. 
a random field choice made by the computer is good enough for the game.

Requirements:
Implement the following features:
- the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax: board[row][column]
- each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
- the board's appearance should be exactly the same as the one presented in the example.
- implement the functions defined for you in the editor.

Drawing a random integer number can be done by utilizing a Python function called randrange(). 
The example program below shows how to use it (the program prints ten random numbers from 0 to 8).

Note: the from-import instruction provides access to the randrange function defined within an external Python module called random.

from random import randrange

for i in range(10):
    print(randrange(8))
'''

from random import randrange

def display_board(board):
	print("+-------" * 3,"+",sep="")
	for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(board):
	ok = False
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("Bad move - repeat your input!")
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		sign = board[row][col]
		ok = sign not in ['O','X'] 
		if not ok:
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O'

def make_list_of_free_fields(board):
	free = []
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ['O','X']:
				free.append((row,col))
	return free


def victory_for(board,sign):
	if sign == "X":
		who = 'me'
	elif sign == "O":
		who = 'you'
	else:
		who = None
	cross1 = cross2 = True
	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
			return who
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
			return who
		if board[rc][rc] != sign:
			cross1 = False
		if board[2 - rc][2 - rc] != sign:
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def draw_move(board):
	free = make_list_of_free_fields(board)
	count = len(free)
	if count > 0:
		this = randrange(count)
		row, col = free[this]
		board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3)]

ro = randrange(3)
co = randrange(3)
board[ro][co] = 'X'
free = make_list_of_free_fields(board)
humanturn = True
while len(free):
	display_board(board)
	if humanturn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	humanturn = not humanturn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")