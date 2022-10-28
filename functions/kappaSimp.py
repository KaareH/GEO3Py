# GEO3, Python port
# kappaSimp
# functions/kappaSimp.py


# Description:
# Auxiliary version of kappa for result presentation only.
# Using 'abs' and symbolic simplification.
#
# Globals: 
# Locals:  kap, rP, rPP
# Parameters: r, L
def kappaSimp(r, L):
	
	
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D), t);
	kap:= unapply(abs(simplify(nrm(crs(rPP(t), rP(t)))/(nrm(rP(t))^3), symbolic)), t);
	kap(L[1]);
	
