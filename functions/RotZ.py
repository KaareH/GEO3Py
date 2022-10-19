# GEO3, Python port
# RotZ
# functions/RotZ.py


# List a rotated angle  t  around z-axis. Output list.
# Globals: 
# Locals:  new
# Parameters: a::list, t
def RotZ(a::list, t):
	
	
	###########################################################
	
	###########################################################
	
	convert(Matrix([
	[cos(t), -sin(t), 0], 
	[sin(t), cos(t), 0],
	[0,0,1]
	]).Vector(a), list); 
	
	
	
	#############################################################
	
