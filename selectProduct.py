import csv

def chooseProduct():

	# GET MER
	# CALCULATE CALORIE INTAKE

	# GET HEALTH ISSUE
	# GET BREED SIZE
	# LIFE SPAN
	# FLAVOURS TO AVOID
	breedSize = 'medium'
	healthIssue = 'gastro'
	lifeSpan = 'puppy'
	flavoursToAvoid = 'chicken'
	temp1 = []
	temp2 = []
	temp3 = []
	final = []
	with open('products.csv', 'rb') as csvFile:
		reader = csv.reader(csvFile, delimiter=',')
		reader.next()
		for row in reader:
			if healthIssue.lower() in row[3].lower():
				temp1.append(row)

		print 'HEALTH ISSUE'
		for i in temp1:
			print i[0]

		for i in temp1:
			if breedSize.lower() in i[2].lower() or 'all' in i[2].lower():
				temp2.append(i)
		
		print 'BREED SIZE'
		for i in temp2:
			print i[0]

		for i in temp2:
			if lifeSpan.lower() in i[1].lower() or 'all' in i[1].lower():
				temp3.append(i)

		print 'LIFE SPAN'
		for i in temp3:
			print i[0]

		for i in temp3:
			if flavoursToAvoid.lower() not in i[5].lower():
				final.append(i)

		print 'FLAVOURS TO AVOID'
		for i in final:
			print i[0]

if __name__ == '__main__':
	chooseProduct()