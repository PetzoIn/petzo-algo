def body_shape(body_Shape):
	
	if (body_Shape=="Severly Underweight"):
		bodys_factor=7

	elif (body_Shape=="Underweight"):	
			bodys_factor=7

	elif (body_Shape=="Ideal"):
			bodys_factor=7

	elif (body_Shape=="Obese"):
			bodys_factor=7
			
	else: 
		bodys_factor=7
	#for test
	print bodys_factor
	return bodys_factor


if __name__ == "__main__":
	body_Shape = "Overweight"
	body_shape(body_Shape)