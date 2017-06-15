import csv

def breed(breedType, breed1, breed2):
	if breedType == 1:
		# single breed
		with open('data.csv') as fi_obj:
			reader = csv.DictReader(fi_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed1:
					dbreed1 = line["Size"]
					print dbreed1
		return dbreed1

	if breedType == 2:
		with open('data.csv') as fi1_obj:
			reader = csv.DictReader(fi1_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed1:
					dbreed2 = line["Size"]
					#print dbreed2

		with open('data.csv') as fi2_obj:
			reader = csv.DictReader(fi2_obj, delimiter=',')
			for line in reader:
				if line["Breed"] == breed2:
					dbreed3 = line["Size"]
					#print dbreed3
		return dbreed2, dbreed3

if 
__name__ == "__main__":
	breedType=2
	breed1="Beagle"
	breed2="Carin Terrier"
	breed(breedType,breed1,breed2)
