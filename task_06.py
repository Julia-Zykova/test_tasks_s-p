def rps_game_winner(arg):
	
	rps = ['R', 'P','S']

	if len(arg) > 2:
		return print('WrongNumberOfPlayersError')

	for i in arg:
		if i[1] not in rps:
			return print('NoSuchStrategyError')


	if arg[0][1] == "R" and arg[1][1] == "P":
		print("'player2 P'")

	elif arg[0][1] == "R" and arg[1][1] == "S":
		print("'player1 R'")

	elif arg[0][1] == "P" and arg[1][1] == "S":
		print("'player2 S'")

	elif arg[0][1] == "P" and arg[1][1] == "R":
		print("'player1 P'")

	elif arg[0][1] == "S" and arg[1][1] == "R":
		print("'player2 R'")

	elif arg[0][1] == "S" and arg[1][1] == "P":
		print("'player1 S'")

	elif arg[0][1] == arg[1][1]:
		print(f"'player1 {arg[0][1]}'")




rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])