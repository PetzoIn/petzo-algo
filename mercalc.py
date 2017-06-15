def mer_function(rer, act_lvl, body_condition,totalMonths,pregnant,neutered,size)
	if size == 1:
		#small
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=8:
			if neutered == 1:
				factor = 2
		elif totalMonths>8:
			factor = 1.8

	elif size == 2 or size == 3:
		# medium or large
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=12:
			factor = 2
		elif totalMonths>12:
			factor = 1.8

	elif size == 4:
		# giant
		if totalMonths>0 and totalMonths<=4:
			factor = 3
		elif totalMonths>4 and totalMonths<=18:
			factor = 2
		elif totalMonths>18:
			factor = 1.8


