# GEO3, Python port
# FII
# functions/FII.py


# Description:
# Calculates the second fundamental form FII as a matrix from given 
# parametrization r. Out parameters or values are specified in given 2-element list L
#
# Globals: 
# Locals:  rPPuu, rPPuv, rPPvv, Lr, Mr, Nr, Ur, sec
# Parameters: r, L
def FII(r, L):
	
	
	      
	#####################################################################
	      rPPuu := unapply(convert(diff(r(u,v), u,u),D), u,v):
	      rPPuv := unapply(convert(diff(r(u,v), u,v),D), u,v):
	      rPPvv := unapply(convert(diff(r(u,v), v,v),D), u,v):
	      Ur:= unapply(UnitSurfNormal(r, [u,v]), u,v);
	      Lr:= unapply(simplify(dot(rPPuu(u,v), Ur(u,v))), u,v):
	      Mr:= unapply(simplify(dot(rPPuv(u,v), Ur(u,v))), u,v):
	      Nr:= unapply(simplify(dot(rPPvv(u,v), Ur(u,v))), u,v):
	      sec:= unapply([[Lr(u,v), Mr(u,v)], [Mr(u,v), Nr(u,v)]], u,v):
	      Matrix(2,2, sec(L[1], L[2]));
	
