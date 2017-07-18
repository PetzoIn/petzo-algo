import math
from adult_mer_cat import *

def pregnancy(weight,adult_mer, pmonth):
	if (pmonth=="1"):
		preg_mer = 0
	else:
		preg_mer = adult_mer * 0.25
	return preg_mer

def lactation(npups, weight):
	if (npups<3):
		lactation=18
	elif (npups<5):
		lactation=60
	elif (npups>4):
		lactation=70
	# 1 here is for the omiitted constraint of lact months
	lact_mer = lactation*weight*1
	return lact_mer

