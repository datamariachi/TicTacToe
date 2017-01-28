positions = [1,2,3,4,5,6,7,8,9]
winning_combinations = [set([1,2,3]),set([4,5,6]),set([7,8,9]),set([1,4,7]),set([2,5,8]),set([3,6,9]),set([1,5,9]),set([3,5,7])]
player_1 = []
player_2 = []

def get_board(positions):
	for i in range(3):
		for j in range(3):
			print("\t" + str(positions[i*3+j]) , sep = " | ", end = "  ")
			print(" | ", end = " ")
		print()
		if i <= 1:
			print("\t---------------------")
	print()


def get_input( action ):
	print()
	movement = input( action )
	return int(movement)

def change( player , symbol ):
	action = get_input("\tIngresa tu tiro:  ")
	number = positions.pop( int(action) - 1 )  
	positions.insert( int(action) - 1 , symbol)
	player.append(number) 
	print()

def say_welcome():
	print()
	print("                                     Welcome to my TicTacToe game, Are you ready?")
	print()

def winner():
	set_player_1 = set(player_1)
	set_player_2 = set(player_2)
	for i in range(8):
		if winning_combinations[i].issubset(set_player_1) or winning_combinations[i].issubset(set_player_2):
			return False
	return True

def tictactoe():
	say_welcome()
	tiros = 0
	turn = True
	while tiros < 9 and winner():
		tiros += 1
		get_board( positions )
		if turn:
			change(player_1 , "X")
		else:
			change(player_2 , "O")
		turn = not turn
	get_board(positions)
	print("                              Thanks for playing!")

tictactoe()
