import math
from body_shape_activity_factor	import *

def cat_mer(body_factor_net,weight,totalMonths,body_Activity,power):
	
	if (totalMonths<5):
		adult_mer = 250*weight
	
	elif (totalMonths<8):
		adult_mer = 130*weight
	
	elif(totalMonths<13):
		adult_mer = 100*weight

	elif(totalMonths<120):
		adult_mer = body_factor_net*(weight**power)
	
	elif(totalMonths>119):
		adult_mer = 45*weight

	print '\n'
	print "mer 1 calculated"
	
	return adult_mer

