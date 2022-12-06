# GEO3, Python port
# kappaTrunc
# functions/kappaTrunc.py


# Description:
# Auxiliary version of kappa for display purposes.
# This version is only infty if tangent vector vanishes.
#
# Globals: 
# Locals:  kap, rP, rPP
# Parameters: r, L
def kappaTrunc(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	rP:= unapply(convert(diff(r(t),t), D),t)
	rPP:= unapply(convert(diff(rP(t),t), D), t)
	kap:= unapply(evalf((nrm(crs(rPP(t), rP(t))))/(0.0000001+ nrm(rP(t))^3)), t)
	kap(L[1])
	
##################################
########## ORIGINAL ##############
##################################
	
	
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D), t);
	kap:= unapply(evalf((nrm(crs(rPP(t), rP(t))))/(0.0000001+ nrm(rP(t))^3)), t);
	kap(L[1]);
	
