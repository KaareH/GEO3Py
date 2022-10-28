# GEO3, Python port
# deprecated_deformAnimLin
# functions/deprecated_deformAnimLin.py


# Description:
# Display of animated deformation from first surface r1 
# to second surface r2 via (1-t)*r1(u,v) + t*r2(u,v) from common parameter 
# domain for (u,v). The integer frames is number of figures in one way sequence
#
# Globals: 
# Locals:  tt
# Parameters: r1, r2, Br, netr, frames
def deprecated_deformAnimLin(r1, r2, Br, netr, frames):
	
	
	
	#####################################################################
	
	display([seq(wireFrameSurfaceBound(
	(u,v)-> convert(evalm(((frames-tt)/frames)*r1(u,v) + (tt/frames)*r2(u,v)), list), 
	Br, netr), tt=0...frames)], insequence=true);
	
	
