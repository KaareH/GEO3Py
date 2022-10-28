# GEO3, Python port
# K
# functions/K.py


# Description:
# Calculates the Gaussian curvature of regular surface from given 
# parametrization r. Out parameters or values are specified in given 2-element list L
#
# Globals: 
# Locals:  efg, e,f,g,lmn,l,m,n,gauss
# Parameters: r, L
def K(r, L):
	
	
	
	#####################################################################
	efg:= EFG(r, [u,v]);  
	e:= efg[1];
	f:= efg[2];
	g:= efg[3];
	lmn:= LMN(r, [u,v]);
	l:= lmn[1];
	m:= lmn[2];
	n:= lmn[3];
	gauss:= unapply(simplify((l*n-m^2)/(e*g-(f^2))), u,v);
	gauss(L[1], L[2]);
	
	
