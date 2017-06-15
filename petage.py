import datetime

def age(dob=False, year=None, month=None):
	if dob:
		# calculate age
		today = datetime.date.today()
		todayYear = today.year
		todayMonth = today.month

		if todayMonth > month:
			yearDuration = abs(y-year)
			monthDuration = todayMonth-month
		else:
			yearDuration = abs(y-year)
			yearDuration-=1
			monthDuration = 12-month+todayMonth

	else:
		yearDuration = year
		monthDuration = month

	totalMonths = yearDuration*12 + monthDuration

	'''
	if size == 1:
		# small
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=8:
			factor = 2
		elif totalMonths>8:
			factor = 1.8

	elif size == 2 or size == 3:
		# medium or large
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=12:
			factor = 2
		elif totalMonths>12:
			factor = 1.8

	elif size == 4:
		# giant
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=18:
			factor = 2
		elif totalMonths>18:
			factor = 1.8
	'''
	return totalMonths