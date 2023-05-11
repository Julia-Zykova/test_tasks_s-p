def date_in_future(integer):
	import datetime
	from datetime import timedelta

	date =  datetime.datetime.now()

	if type(integer) != int:
		print(date.strftime("%d-%m-%Y %H:%M:%S'"))

	else: 
		future_date= date + timedelta(hours = integer * 24)
		print(future_date.strftime("%d-%m-%Y %H:%M:%S'"))

date_in_future([])
date_in_future(2)