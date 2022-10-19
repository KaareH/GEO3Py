# GEO3, Python port
# kappa
# functions/kappa.py


# 
# Globals: 
# Locals:  kap, rP, rPP
# Parameters: r, L
def kappa(r, L):
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D), t);
	kap:= unapply(simplify(nrm(crs(rPP(t), rP(t)))/(nrm(rP(t))^3)), t);
	kap(L[1]);
	
