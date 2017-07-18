def body_shape(body_Shape):
	power=0.67
	if (body_Shape=="Severly Underweight"):
		bodys_factor=95

	elif (body_Shape=="Underweight"):	
			bodys_factor=95

	elif (body_Shape=="Ideal"):
			bodys_factor=100

	elif (body_Shape=="Obese"):
			bodys_factor=130
			power=0.4
	
	else: 
		bodys_factor=130
		power=0.4
	#for test
	print '\n'

	print "body shape"
	print bodys_factor
	return bodys_factor, power


if __name__ == "__main__":
	body_Shape = "Overweight"
	body_shape(body_Shape)