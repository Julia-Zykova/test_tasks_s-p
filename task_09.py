def connect_dicts(dict1, dict2):

	dict3 = {}
	keys1 = []
	keys2 = []
	sum_val1 = 0
	sum_val2 = 0

	for k,v in dict1.items():
		sum_val1 +=v
		keys1.append(k)

	for k,v in dict2.items():
		sum_val2 +=v
		keys2.append(k)

	for k in keys1:
		if dict1[k] >= 10:
			if k in keys2:
				if sum_val1 > sum_val2:
					dict3[k] = dict1[k]
				elif sum_val1 == sum_val2:
					dict3[k] =dict2[k]
			
			else:
				dict3[k] = dict1[k]

	for k in keys2:
		if dict2[k] >= 10:
			if k not in keys1:
				dict3[k] = dict2[k]

	sorted_list = sorted(dict3.items(),reverse = True)
	sorted_dict3 = {k: v for k, v in sorted_list}
	
	return sorted_dict3


connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })