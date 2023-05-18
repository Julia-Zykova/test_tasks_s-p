def rps_game_winner(arg):
	
	rps = ['R', 'P','S']

	first_player = arg[0][0]
	second_player = arg[1][0]
	first_player_move = arg[0][1]
	second_player_move = arg[1][1]


	try:
		if len(arg) > 2:
			raise Exception('WrongNumberOfPlayersError')

	except Exception:
		return 'WrongNumberOfPlayersError'

	try:
		for i in arg:
			if i[1] not in rps:
				raise Exception('NoSuchStrategyError')
	except Exception:
		return 'NoSuchStrategyError'


	if first_player_move == "R" and second_player_move == "P":
		return (f"{second_player} {second_player_move}")

	elif first_player_move == "R" and second_player_move == "S":
		return (f"{first_player} {first_player_move}")

	elif first_player_move == "P" and second_player_move == "S":
		return (f"{second_player} {second_player_move}")

	elif first_player_move == "P" and second_player_move == "R":
		return (f"{first_player} {first_player_move}")

	elif first_player_move == "S" and second_player_move == "R":
		return (f"{second_player}  {second_player_move}")

	elif first_player_move == "S" and second_player_move == "P":
		return (f"{first_player} {first_player_move}")

	elif first_player_move == second_player_move:
		return (f"{first_player} {first_player_move}")


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])