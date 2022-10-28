# GEO3, Python port
# LMN
# functions/LMN.py


# Description:
# Calculates the 3 components L, M, and N as a list
# [L, M, N] from given parametrization r. 
# Out parameters or values are specified in given 2-element list L
#
# Globals: 
# Locals:  rPPuu, rPPuv, rPPvv, Lr, Mr, Nr, Ur
# Parameters: r, L
def LMN(r, L):
	
	
	      
	#####################################################################
	      rPPuu := unapply(convert(diff(r(u,v), u,u),D), u,v):
	      rPPuv := unapply(convert(diff(r(u,v), u,v),D), u,v):
	      rPPvv := unapply(convert(diff(r(u,v), v,v),D), u,v):
	      Ur:= unapply(UnitSurfNormal(r, [u,v]), u,v);
	      Lr:= unapply(simplify(dot(rPPuu(u,v), Ur(u,v))), u,v):
	      Mr:= unapply(simplify(dot(rPPuv(u,v), Ur(u,v))), u,v):
	      Nr:= unapply(simplify(dot(rPPvv(u,v), Ur(u,v))), u,v):
	      [Lr(L[1], L[2]), Mr(L[1], L[2]), Nr(L[1], L[2])];
	
