import csv

# age = GROWTH/ ADULT/ OLD (TEXT)
# healthIssue = OPTIONS (TEXT)
# skinCoat = ROUGH/SHINY/FAIR (TEXT)
# stoolConsistency = NORMAL/LOOSE/HARD (TEXT)
# unusualSubstance = OPTIONS (TEXT)
def nutrientsComposition(age, healthIssue, skinCoat, stoolConsistency, unusualSubstance):
	nutrientsIndex = 0
	ageIndex = -1
	healthIssueIndex = -1

	n = []
	values = []

	# No health issue
	if not healthIssue:
		healthIssueIndex = -1

	elif 'gastro' in healthIssue.lower():
		healthIssueIndex = 4

	elif 'joint' in healthIssue.lower():
		healthIssueIndex = 5

	elif 'kidney' in healthIssue.lower():
		healthIssueIndex = 6

	elif 'skin' in healthIssue.lower():
		healthIssueIndex = 7

	elif 'diabetes' in healthIssue.lower():
		healthIssueIndex = 8

	elif 'cvd' in healthIssue.lower():
		healthIssueIndex = 9

	elif 'liver' in healthIssue.lower():
		healthIssueIndex = 10

	# Age is Growth
	if 'growth' in age.lower():
		ageIndex = 1

	elif 'adult' in age.lower():
		ageIndex = 2

	elif 'old' in age.lower():
		ageIndex = 3

	with open('diseaseNutrients.csv', 'rb') as csvFile:
		reader = csv.reader(csvFile, delimiter=',')

		if healthIssueIndex != -1:
			for row in reader:
				n.append(row[nutrientsIndex])
				values.append(row[healthIssueIndex])

		else:
			for row in reader:
				n.append(row[nutrientsIndex])
				values.append(row[ageIndex])

		# STOOLCONSISTENCY
		if stoolConsistency.lower() == 'normal':
			pass

		elif stoolConsistency.lower() == 'loose':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Fiber' in n[i]:
					values[i] = values[i]*(0.80)

				elif 'Fat' in n[i]:
					values[i] = values[i]*(0.80)

		elif stoolConsistency.lower() == 'hard':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Vitamin E' in n[i]:
					values[i] = values[i]*(1.30)

				elif 'Fiber' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Fat' in n[i]:
					values[i] = values[i]*(1.20)
					

		# SKIN
		if skinCoat.lower() == 'shiny':
			pass

		elif skinCoat.lower() == 'rough':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Zinc' in n[i]:
					values[i] = values[i]*(1.25)

				elif 'Linoleic' in n[i]:
					values[i] = values[i]*(1.25)

		elif skinCoat.lower() == 'fair':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Choline' in n[i]:
					values[i] = values[i]*(1.10)

				elif 'Linoleic' in n[i]:
					values[i] = values[i]*(1.25)

		# UNUSUALSUBSTANCE
		if 'grass' in unusualSubstance.lower():
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Fiber' in n[i]:
					values[i] = values[i]*(1.20)

		elif 'litter' in unusualSubstance.lower():
			for i in len(n):
				if 'Thiamine' in n[i]:
					values[i] = values[i]*(1.10)

				elif 'Riboflavin' in n[i]:
					values[i] = values[i]*(1.10)

				elif 'Niacin' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Pyridoxine' in n[i]:
					values[i] = values[i]*(1.10)

		elif 'mud' in unusualSubstance.lower():
			for i in range(8,20):
				values[i] = values[i]*(1.1)

		elif 'stool' in unusualSubstance.lower():
			for i in range(20,28):
				values[i] = values[i]*(1.15)

		elif 'cloth' in unusualSubstance.lower():
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Fiber' in n[i]:
					values[i] = values[i]*(1.10)

		elif 'floor' in unusualSubstance.lower():
			for i in len(n):
				if 'Calcium' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Phosphorus' in n[i]:
					values[i] = values[i]*(1.20)

				elif 'Magnesium' in n[i]:
					values[i] = values[i]*(1.10)

		return values