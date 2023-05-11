def max_odd(array):

	odd_num = []
	other = []

	for i in array:

		if (type(i) == int) or (type(i) == float):
			if i % 2 == 1:
				odd_num.append(round(i))

		if type (i) == list:
			for l in i:
				if type(l in i) == int or float:
					odd_num.append(round(l))

	odd_num.sort()

	if len(odd_num) > 0:
		print(odd_num[-1])
	else:
		print(None)
	

max_odd([1, 2, 3, 4, 4])
max_odd([21.0, 2, 3, 4, 4])
max_odd(['ololo', 2, 3, 4, [1, 2], None])
max_odd(['ololo', 'fufufu'])
max_odd([2, 2, 4])