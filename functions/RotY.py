# GEO3, Python port
# RotY
# functions/RotY.py


# Description:
# List a rotated angle  t  around y-axis. Output list.
#
# Globals: 
# Locals:  new
# Parameters: a::list, t
def RotY(a, t):
	
	
	###########################################################
	
	###########################################################
	
	convert(Matrix([
	[cos(t), 0,-sin(t)],
	[0, 1, 0], 
	[sin(t), 0, cos(t)]
	]).Vector(a), list); 
	
	
	
	#############################################################
	
