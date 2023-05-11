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



#Разработайте функцию count_words(string), которая будет возвращать словарь со статистикой частоты употребления входящих в неё слов.

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}