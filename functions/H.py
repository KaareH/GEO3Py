# GEO3, Python port
# H
# functions/H.py


# Calculates the mean curvature of regular surface from given 
parametrization r. Out parameters or values are specified in given 2-element list L
# Globals: 
# Locals:  efg, e,f,g,lmn,l,m,n,mean
# Parameters: r, L
def H(r, L):
	
	
	
	#####################################################################
	efg:= EFG(r, [u,v]);  
	e:= efg[1];
	f:= efg[2];
	g:= efg[3];
	lmn:= LMN(r, [u,v]);
	l:= lmn[1];
	m:= lmn[2];
	n:= lmn[3];
	mean:= unapply(simplify((l*g-2*m*f+n*e)/(2*(e*g-(f^2)))), u,v);
	mean(L[1], L[2]);
	
