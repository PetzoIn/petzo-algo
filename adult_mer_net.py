import math
from adult_mer_dog import *
from adult_dog_preglact import *
from body_shape_activity_factor import *
from bodyactivity import *
from bodyshape import * 
from petage import *
from treats import *


if __name__ == "__main__":
	weight = float(raw_input("Enter weight of pet in kgs "))
	activity = (raw_input("How active is your dog ? Inactive,Ideal,Active,Highly Active "))
	shape = (raw_input("Shape of your dog ?Severly Underweight,Underweight,Ideal,Obese,Overweight "))
 	gender = (raw_input("gender of your dog? "))
 	dob=0
 	year = int(raw_input("Enter birth year "))
 	month = int(raw_input("Enter birth month "))
	if (gender=="Male"):
		neut = (raw_input("Neutered Yes/No "))
	else:
		neut = "No"	
 	#we start calling funct. now
	bodyact = body_activity_neut(activity,neut)
	bodysha = body_shape(shape)
	bodyfact = body_shape_activity_factor(bodysha, bodyact)
	pet_months = age(dob,year,month)

	mer1 = dog_mer(bodyfact,weight,pet_months,activity)
	
	if (gender != "Male"):
		preg = (raw_input("Pregnant(P)/lactation(L)? or Nothing(N) "))
		neut = "No"
		if(preg=="P"):
			preg_month = (raw_input("1 or 2 month? "))
			mer2 = pregnancy(weight,activity,mer1)
		elif(preg=="L"):
			lactation_week = int(raw_input("Enter lactation week 1,2,3,4 "))
			npups = int(raw_input("Enter no. of pups "))
			mer2 = lactation(npups, weight,lactation_week)
		else:
			mer2=0;
	else:
		mer2=0

	mer_net = mer1 + mer2
	
	ntreats = (raw_input("No. of treats SOme(1) alot(2) other (3)"))
 	mer_net_final = treats(ntreats,mer_net)
	print mer_net_final


