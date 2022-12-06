# GEO3, Python port
# EFG
# functions/EFG.py


# Description:
# Calculates the 3 metric matrix components as a list
# [E, F, G] from given parametrization r. 
# Out parameters or values are specified in 2-element list L
#
# Globals:  E,F,G
# Locals:  rP1,rP2, Er, Fr, Gr
# Parameters: r, L
def EFG(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	
	rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	Er:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	Fr:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	Gr:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	[Er(L[1], L[2]), Fr(L[1], L[2]), Gr(L[1], L[2])]
	
##################################
########## ORIGINAL ##############
##################################
	
	
	      
	      
	      rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	      rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	      Er:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	      Fr:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	      Gr:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	      [Er(L[1], L[2]), Fr(L[1], L[2]), Gr(L[1], L[2])];
	
