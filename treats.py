def treats(ntrets,adult_mer):
	if (ntrets==1):
		#for small amt of treats
		adult_mer = adult_mer*0.95
	elif (ntrets==2):
		#a lot of treats
		adult_mer = adult_mer*0.9
	else: 
		#for other options 3 etc.
		pass
	return adult_mer
	
