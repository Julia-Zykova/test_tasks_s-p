def count_words(string):
	import re

	d = {}

	string = re.sub(r"[.,!?'-]","", string)
	string = string.split()
	string = [str(s.lower()) for s in string]

	for s in string:
		
		ind = [a for a in range(len(string)) if string[a] == s]
		d[s] = string.count(s)

	print(d)


count_words("A man, a plan, a canal -- Panama") 
count_words("Doo bee doo bee doo") 