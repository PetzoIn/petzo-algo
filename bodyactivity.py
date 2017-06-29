def body_activity(body_Activity):
	
	if (body_Activity=="Inactive"):
		bodya_factor=95

	elif (body_Activity=="Ideal"):	
			bodya_factor=110

#	elif (body_Activity=="Active"):
#			bodya_factor=130

#	elif (body_Activity=="Highly Active"):
#			bodya_factor=7
	else: 
		bodya_factor=130
	#for test
	print bodya_factor
	return bodya_factor


if __name__ == "__main__":
	body_Activity = "Ideal"
	body_activity(body_Activity)