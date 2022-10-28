# GEO3, Python port
# tau
# functions/tau.py


# Description:
No description provided
#
# Globals: 
# Locals:  ta, rP, rPP, rPPP
# Parameters: r, L
def tau(r, L):
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D), t);
	rPPP:= unapply(convert(diff(rPP(t),t), D), t);
	ta:= unapply(simplify(dot(rPPP(t), crs(rP(t), rPP(t)))/nrm(crs(rPP(t), rP(t)))^2), t);
	ta(L[1]);
	
