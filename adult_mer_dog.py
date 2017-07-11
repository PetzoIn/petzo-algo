import math
from body_shape_activity_factor	import *

def dog_mer(body_factor_net,weight,totalMonths,body_Activity):
	adult_mer = body_factor_net*(weight**0.75)
	
	if (totalMonths<5):
		adult_mer = 2*adult_mer
	
	elif (totalMonths<9):
		adult_mer = 1.6*adult_mer
	
	elif(totalMonths<13):
		adult_mer = 1.2*adult_mer
	
	elif(totalMonths>96):
		#geriatrics case or OLD dog
		if (body_Activity=="Active"):
			adult_mer = 105*(weight**0.75)
		else:
			adult_mer = 95*(weight**0.75)
	
	else:
		adult_mer = adult_mer

	print '\n'
	print "mer 1 calculated"
	
	return adult_mer

