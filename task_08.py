def multiply_numbers(inputs = []):
	from functools import reduce


	inputs = ((str(inputs)).split(".")) if (type(inputs) == float) else list(inputs)
	
	new_list = []

	for i in inputs:

		if (type(i) == str):

			try:
				i = int(i)
				new_list.append(i)
					
			except:
				pass

		elif (type(i) == int):
			new_list.append(i)

		else:
			pass
		
	try:
		result = reduce((lambda a,b: a*b), (i for i in new_list))
		print(result)

	except:
		print(None)

multiply_numbers()
multiply_numbers('ss')
multiply_numbers('1234')
multiply_numbers('sssdd34')
multiply_numbers(2.3)
multiply_numbers([5, 6, 4])