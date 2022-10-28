# GEO3, Python port
# RotX
# functions/RotX.py


# Description:
# List a rotated angle  t  around x-axis
#
# Globals: 
# Locals:  new
# Parameters: a::list, t
def RotX(a, t):
	
	
	###########################################################
	
	###########################################################
	
	convert(Matrix([
	[1, 0,0],
	[0, cos(t), -sin(t)], 
	[0, sin(t), cos(t)]
	]).Vector(a), list); 
	
	
	
	#############################################################
	
