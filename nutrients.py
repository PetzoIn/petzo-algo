import csv

def nutrientsComposition(age, healthIssue, skin, stoolConsistency, unusualSubstance):
	nutrientsIndex = 0
	ageIndex = -1

	# No health issue
	if healthIssue is unicode(''):
		healthIssue = -1

	# Age is Growth
	if 'growth' in age.lower():
		ageIndex = 1

	elif 'adult' in age.lower():
		ageIndex = 2

	elif 'old' in age.lower():
		ageIndex = 3


	with open('diseaseNutrients.csv', 'rb') as csvFile:
		csvFile = csv.reader(csvFile, delimiter=',')

