import csv

def breed(breedType, breed1, breed2):
	if breedType == 1:
		# single breed
		with open('data.csv') as fi_obj:
			reader = csv.DictReader(fi_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed1:
					dbreed1 = line["Size"]
		
		#test only
		print dbreed1			
		return dbreed1

	if breedType == 2:
		with open('data.csv') as fi1_obj:
			reader = csv.DictReader(fi1_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed1:
					dbreed2 = line["Size"]
					

		with open('data.csv') as fi2_obj:
			reader = csv.DictReader(fi2_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed2:
					dbreed3 = line["Size"]

		if (dbreed2==dbreed3):
			dbreed4=dbreed2
		elif (dbreed2>=3 and dbreed3>=3):
			dbreed4=4
		elif ((dbreed2+dbreed3)<5):
			dbreed4=2
		else:
			dbreed4=3
		#test only
		#print dbreed2, dbreed3
		#dbreed4 = dbreed2
		return dbreed4


if __name__ == "__main__":
	breedType=2
	breed1="Beagle"
	breed2="Carin Terrier"
	breed(breedType,breed1,breed2)
