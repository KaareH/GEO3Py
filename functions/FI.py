# GEO3, Python port
# FI
# functions/FI.py


# Description:
# Calculates the metric matrix FI from given 
# parametrization r. Out parameters or values are specified in 2-element list L
#
# Globals: 
# Locals:  rP1,rP2, E, F, G, met
# Parameters: r, L
def FI(r, L):
	
	
	      
	      rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	      rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	      E:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	      F:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	      G:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	      met:= unapply([[E(u,v), F(u,v)], [F(u,v), G(u,v)]], u,v):
	      Matrix(2,2, met(L[1], L[2]));
	
