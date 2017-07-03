#!/usr/bin/python

from bodyactivity import *
from bodyshape import *

def body_shape_activity_factor(bodys_factor, bodya_factor):
	body_factor_net = (bodya_factor+bodys_factor)*0.5
	#testz	
	print '\n'
	print 'shape, activity'
	print body_factor_net
	return body_factor_net

if __name__ == "__main__":
		body_Activity = "Ideal"
		body_Shape = "Overweight"
		neut_status = "No"
		body_shape_activity_factor(body_activity_neut(body_Activity,neut_status),body_shape(body_Shape))
