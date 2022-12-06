# GEO3, Python port
# deprecated_deformAnimTrig
# functions/deprecated_deformAnimTrig.py


# Description:
# Display of animated deformation from first surface r1 
# to second surface r2 and back via cos(t)*r1(u,v) + sin(t)*r2(u,v) from common parameter 
# domain for (u,v). The integer frames is number of figures in full rotation sequence.
#
# Globals: 
# Locals:  tt
# Parameters: r1, r2, Br, netr, frames
def deprecated_deformAnimTrig(r1, r2, Br, netr, frames):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	#####################################################################
	
	display([seq(wireFrameSurfaceBound(
	(u,v)-> convert(evalm(cos(tt*2*Pi/frames)*r1(u,v) + sin(tt*2*Pi/frames)*r2(u,v)), list),
	Br, netr), tt=0...frames)], insequence=true)
	
	
##################################
########## ORIGINAL ##############
##################################
	
	
	
	#####################################################################
	
	display([seq(wireFrameSurfaceBound(
	(u,v)-> convert(evalm(cos(tt*2*Pi/frames)*r1(u,v) + sin(tt*2*Pi/frames)*r2(u,v)), list), 
	Br, netr), tt=0...frames)], insequence=true);
	
	
