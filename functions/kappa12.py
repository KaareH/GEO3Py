# GEO3, Python port
# kappa12
# functions/kappa12.py


# Description:
# Calculates the principal curvatures (in list form) of regular surface from given 
# parametrization r. Out parameters or values are specified in given 2-element list L
#
# Globals: 
# Locals:  K, H, kap
# Parameters: r, L
def kappa12(r, L):
	
	
	
	#####################################################################
	K:= GaussC(r, [u,v]);
	H:=  meanC(r, [u,v]);
	kap:= unapply(simplify([H+sqrt(H^2 - K), H-sqrt(H^2-K)]), u,v);
	kap(L[1], L[2]);
	
