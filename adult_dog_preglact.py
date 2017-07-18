import math
from adult_mer_dog import *

def pregnancy(weight,body_Activity,adult_mer):
	if (body_Activity=="Active"):
		preg_mer = 0.5 * adult_mer
	else:
		preg_mer = adult_mer * 0.5
	return preg_mer

def lactation(npups, weight,lactation_week):
	#m = npups - 4
	if (npups>4):
		m=n-4
	else:
		m=0
	lact_mer = weight*(24*npups + 12*m)
	return lact_mer

