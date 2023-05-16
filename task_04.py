def sort_list(list):

	new_list = []
	min_num = []
	max_num = []

	if len(list) > 0:
		min_num = min(list)
		max_num = max(list)
		min_num, max_num = max_num, min_num

		for i in list:
			if (i != min(list)) and (i != max(list)):
				new_list.append(i)

			elif i == min(list):
				new_list.append(min_num)
				if len(list) == 1:
					new_list.append(min_num)

			elif i == max(list):
				
				new_list.append(max_num)
				new_list.append(max_num)

		
	return new_list

sort_list([])
sort_list([2, 4, 6, 8])
sort_list([1])
sort_list([1, 2, 1, 3])
