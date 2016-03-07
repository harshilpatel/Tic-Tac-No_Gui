# Author: Harshil Patel
# Contact: harshil912@gmail.com
# Python3

player1 = player2 = ''

board_size = int(input("Board size: "))
still_playing = True

player1 = input("Player1")
player2 = input("Player2")
board = []
for i in range(board_size):
	board.append([])
	for j in range(board_size):
		board[i].append("-")

def if_won(board):
	won = False
	try:
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] != '-':
					player = board[i][j]
					for row in [-1,0,1]:
						if board[i+row][j] != player:
							break
					else:
						won = True
					for column in [-1,0,1]:
						if board[i][j+column] != player:
							break
					else:
						won = True
		return won
		print(won)
	except Exception as e:
		print(e)
		return won

def print_boards(board):
	board_column = '   '
	for i in range(len(board)):
		board_column += str(i) + " "
	print(board_column)

	for i in range(len(board)):
		temp_row = str(i) +"  "
		for j in range(len(board)):
			temp_row += str(board[i][j]) + " "
		print(temp_row)

current_player = 0
while True:
	if current_player%2 == 0: print( player1 + " : Enter x and y Co-ordinates X with space")
	else: print(player2 + " : Enter x and y Co-ordinates 0 with space")
	x = input().strip().split()
	y = int(x[1])
	x = int(x[0])
	if current_player%2 == 0: board[y][x] = 'X'
	else: board[y][x] = '0'

	current_player +=1
	print_boards(board)
	if if_won(board):
		if current_player%2 == 0: print(player1.upper() + " : WON")
		else: print(player2.upper() + " : WON")
		break
	print("\n\n")
	pass
