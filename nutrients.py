import csv

def nutrientsComposition(age, healthIssue, skin, stoolConsistency, unusualSubstance):
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

		# SKIN
		if skin.lower() == 'shiny':
			pass

		elif skin.lower() == 'rough':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Zinc' in n[i]:
					values[i] = values[i]*()

				elif 'Linoleic' in n[i]:
					values[i] = values[i]*()

		elif skin.lower() == 'fair':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Choline' in n[i]:
					values[i] = values[i]*()

				elif 'Linoleic' in n[i]:
					values[i] = values[i]*()

		# STOOLCONSISTENCY
		if stoolConsistency.lower() == 'normal':
			pass

		elif stoolConsistency.lower() == 'loose':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Fiber' in n[i]:
					values[i] = values[i]*()

				elif 'Fat' in n[i]:
					values[i] = values[i]*()

		elif stoolConsistency.lower() == 'hard':
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Vitamin E' in n[i]:
					values[i] = values[i]*()

				elif 'Fiber' in n[i]:
					values[i] = values[i]*()

				elif 'Fat' in n[i]:
					values[i] = values[i]*()

		# UNUSUALSUBSTANCE
		if 'grass' in unusualSubstance.lower():
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Fiber' in n[i]:
					values[i] = values[i]*()

		elif 'litter' in unusualSubstance.lower():
			for i in len(n):
				if 'Thiamine' in n[i]:
					values[i] = values[i]*()

				elif 'Riboflavin' in n[i]:
					values[i] = values[i]*()

				elif 'Niacin' in n[i]:
					values[i] = values[i]*()

				elif 'Pyridoxine' in n[i]:
					values[i] = values[i]*()

		elif 'mud' in unusualSubstance.lower():
			for i in range(8,20):
				values[i] = values[i]*(1.1)

		elif 'stool' in unusualSubstance.lower():
			for i in range(20,28):
				values[i] = values[i]*(1.15)

		elif 'grass' in unusualSubstance.lower():
			for i in len(n):
				if 'Vitamin A' in n[i]:
					values[i] = values[i]*()

				elif 'Fiber' in n[i]:
					values[i] = values[i]*()

		elif 'floor' in unusualSubstance.lower():
			for i in len(n):
				if 'Calcium' in n[i]:
					values[i] = values[i]*()

				elif 'Phosphorus' in n[i]:
					values[i] = values[i]*()

				elif 'Magnesium' in n[i]:
					values[i] = values[i]*()

		return values