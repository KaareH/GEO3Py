# GEO3, Python port
# UnitSurfNormal
# functions/UnitSurfNormal.py


# Description:
# Calculates the unit surface normal for a surface 
# from given parametrization r. NB: No check for regularity is included, so
# division by 0 is a possible error message.
# Out parameters or values are specified in the 2-element list L
#
# Globals: 
# Locals:  rPu, rPv, Ur, Nor
# Parameters: r, L
def UnitSurfNormal(r, L):
	
	
	      
	#####################################################################
	      rPu:= unapply(convert(diff(r(u,v), u), D), u,v):
	      rPv:= unapply(convert(diff(r(u,v), v), D), u,v):
	      Nor:= unapply(crs(rPu(u,v), rPv(u,v)), u,v);
	      Ur:= unapply(
	               simplify(
	                   convert(
	                       evalm(
	                           Nor(u,v)/nrm(Nor(u,v))
	                             ),
	                       list)
	                        ), 
	                u,v);
	      Ur(L[1], L[2]);
	
