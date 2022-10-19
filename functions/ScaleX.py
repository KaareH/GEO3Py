# GEO3, Python port
# ScaleX
# functions/ScaleX.py


# List a scaled on first coordinate by k
# Globals: 
# Locals:  new
# Parameters: a::list, k
def ScaleX(a::list, k):
	
	
	###########################################################
	
	###########################################################
	
	if nops(a)=2 then
	[k*a[1], a[2]]
	else [k*a[1], a[2], a[3]]
	end if
	
	#############################################################
	
