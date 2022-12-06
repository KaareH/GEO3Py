# GEO3, Python port
# FIdot
# functions/FIdot.py


# Description:
# Calculates the scalar product of vectors v and w at parameter point (L[1], L[2]) from given 
# parametrization r. Out parameters or values are as specified in 2-element list L
#
# Globals: 
# Locals:  rP1,rP2, u,v, E, F, G, scal
# Parameters: r, vec1, vec2, L
def FIdot(r, vec1, vec2, L):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	E:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	F:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	G:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	scal:= (u,v)-> simplify(vec1[1]*E(u,v)*vec2[1] + vec1[1]*F(u,v)*vec2[2]  + vec1[2]*F(u,v)*vec2[1] + vec1[2]*G(u,v)*vec2[2])
	scal(L[1], L[2])
	
##################################
########## ORIGINAL ##############
##################################
	
	
	      
	      rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	      rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	      E:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	      F:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	      G:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	scal:= (u,v)-> simplify(vec1[1]*E(u,v)*vec2[1] + vec1[1]*F(u,v)*vec2[2]  + vec1[2]*F(u,v)*vec2[1] + vec1[2]*G(u,v)*vec2[2]);
	scal(L[1], L[2]);
	
