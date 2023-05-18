def combine_anagrams(words_array):
	
	list_sort = [sorted(list(w.lower())) for w in words_array]
	new_array = []

	for l in list_sort:
		ind = [a for a in range(len(list_sort)) if list_sort[a] == l]
		list_anagr = []

		for i in ind:
			if (list_sort.count(l) == len(ind)) and (len(ind) > 1):
				if (words_array[i]) not in list_anagr:
					list_anagr.append(words_array[i])
				

		if len(ind) == 1:
			for x in (ind):
				non_repeating_word = []
				non_repeating_word.append(words_array[x])
				new_array.append(non_repeating_word)
		else:
			if list_anagr not in new_array:
				new_array.append(list_anagr)
				
		
	return new_array


combine_anagrams([
	"cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream",
	]) 