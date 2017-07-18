def body_activity_neut(body_Activity, neut_status):

	if (neut_status=="No"):
		if (body_Activity=="Inactive"):
			bodya_factor=75

		elif (body_Activity=="Ideal"):	
			bodya_factor=75

		elif (body_Activity=="Active"):
			bodya_factor=100

		elif (body_Activity=="Highly Active"):
			bodya_factor=100
		#else: 
			#applicable for active and highly active
		#	bodya_factor=130
		#for test
	else:
		if (body_Activity=="Inactive"):
			bodya_factor=52

		elif (body_Activity=="Active"):	
				bodya_factor=75

	#	elif (body_Activity=="Active"):
	#			bodya_factor=130

	#	elif (body_Activity=="Highly Active"):
	#			bodya_factor=7
		else: 
			#applicable for active and highly active
			bodya_factor=75
	print '\n'
	print "body activity"	
	print bodya_factor
	return bodya_factor


if __name__ == "__main__":
	body_Activity = "Ideal"
	neut_status = "No"
	body_activity(body_Activity)