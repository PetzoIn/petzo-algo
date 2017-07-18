from adult_mer_net import *
from adult_mer_net_cat import *
from nutrients import *
from selectProduct import *
from petbreed import *

if __name__ == "__main__":
	animal = raw_input("Dog or Cat? ")
	if (animal=="Dog"):
		mer, age = mer_dog()
		if (age<13):
			dog_life="puppy"
			dog_life1="GROWTH"
		elif (age<110):
			dog_life="adult"
			dog_life1="ADULT"
		else:
			dog_life="senior"
			dog_life1="OLD"
		healthIssue=(raw_input("Health issues?(gastro,joint,kidney,skin,diabetes,cvd,liver) "))	
		values = nutrientsComposition(dog_life1, healthIssue)
		print "Nutrients are"
		print values
		print '\n'
		
		breedz=(raw_input("1 or 2 breed "))
		if (breedz=="1"):
			breedType=1
			breed1=(raw_input("What's your breed "))
			breed2="das"
		else:
			breedType=2
			breed1=(raw_input("What's his Breed1 "))
			breed2=(raw_input("What's his Breed2 "))

		flavorAvoid=(raw_input("Flavors to avoid? egg, chicken, lamb, fish, none, other "))
		breedN = breed(breedType, breed1, breed2)

		if(breedN=="1"):
			breedSize="small"
		elif(breedN=="2"):
			breedSize="medium"
		elif(breedN=="3"):
			breedSize="large"
		elif(breedN=="4"):
			breedSize="giant"
		chooseProduct(healthIssue, breedSize, dog_life, flavorAvoid)

	else:
		mer, age = mer_cat()
		if (age<13):
			cat_life="puppy"
		elif (age<110):
			cat_life="adult"
		else:
			cat_life="senior"
