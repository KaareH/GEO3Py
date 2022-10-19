# GEO3, Python port
# kappaNormal
# functions/kappaNormal.py


# Calculates the normal curvature along any regular 
curve (specified in parameter domain by gamU(t)) on surface r(u,v) 
Regularity check is not performed in procedure - division by zero may 
thence occur as error-message. Note that the sign of the normal curvature is 
parametrization dependent. If N is flipped, then the normal curvature is reversed.
Output normal curvature is given at value (or parameter) specified in 
one-element list L.
# Globals: 
# Locals:  F2, gamUP, gamUPunit, kn
# Parameters: r, gamU, L
def kappaNormal(r, gamU, L):
	
	
	
	#####################################################################
	
	F2:= unapply(FII(r, gamU(t)), t);
	gamUP:= unapply(convert(diff(gamU(t), t), D), t);
	gamUPunit:= unapply(convert(evalm(gamUP(t)/FInrm(r, gamUP(t), gamU(t))), list), t);
	
	kn:= unapply(evalm(transpose(gamUPunit(t))&*F2(t)&*gamUPunit(t)), t);
	
	kn(L[1]);
	
	#####################################################################
	
