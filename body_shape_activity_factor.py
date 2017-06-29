from bodyactivity import *
from bodyshape import *

def body_shape_activity_factor(bodys_factor, bodya_factor):
	body_factor_net = (bodya_factor+bodys_factor)*0.5
	#testz
	print 'asdas'
	print body_factor_net
	return body_factor_net

if __name__ == "__main__":
		body_Activity = "Ideal"
		body_Shape = "Overweight"
		body_shape_activity_factor(body_activity(body_Activity),body_shape(body_Shape))
