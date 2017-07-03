import math
from adult_mer_dog import *

def pregnancy(weight,body_Activity,adult_mer):
	if (body_Activity=="Active"):
		preg_mer = 130*26*weight
	else:
		preg_mer = adult_mer * 0.5
	return preg_mer

def lactation(npups, weight,lactation_week):
	m = npups - 4
	if (lactation_week==1):
		lactation=0.75
	elif (lactation==2):
		lactation=0.95
	elif (lactation==3):
		lactation=1.1
	else:
		lactation=1.2
	lact_mer = weight*(24*npups + 12*m)*lactation
	return lact_mer

