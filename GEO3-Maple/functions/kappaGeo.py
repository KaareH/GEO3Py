# GEO3, Python port
# kappaGeo
# functions/kappaGeo.py


# Description:
# Calculates the geodesic curvature along any regular 
# curve (specified in parameter domain by gamU(t)) on surface r(u,v) 
# Regularity check is not performed in procedure - division by zero may 
# thence occur as error-message. Note that the sign of the geodesic curvature is 
# parametrization dependent. If N is flipped, then the normal curvature is reversed.
# Output geodesic curvature is given at value (or parameter) specified in 
# one-element list L.
#
# Globals: 
# Locals:  gam, gamP, gamPP, kapG, lentri
# Parameters: r, gamU, L
def kappaGeo(r, gamU, L):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	#####################################################################
	
	gam:=  unapply(r(gamU(t)[1], gamU(t)[2]), t)
	gamP:= unapply(convert(diff(gam(t), t), D), t)
	gamPP:= unapply(convert(diff(gam(t), t,t), D), t)
	lentri:= unapply(nrm(gamP(t), gamP(t))^3, t)
	
	kapG:= unapply(dot(gamPP(t), crs(UnitSurfNormal(r, gamU(t)), gamP(t)))/lentri(t), t)
	
	kapG(L[1])
	
	#####################################################################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	
	#####################################################################
	
	gam:=  unapply(r(gamU(t)[1], gamU(t)[2]), t);
	gamP:= unapply(convert(diff(gam(t), t), D), t);
	gamPP:= unapply(convert(diff(gam(t), t,t), D), t);
	lentri:= unapply(nrm(gamP(t), gamP(t))^3, t);
	
	kapG:= unapply(dot(gamPP(t), crs(UnitSurfNormal(r, gamU(t)), gamP(t)))/lentri(t), t);
	
	kapG(L[1]);
	
	#####################################################################
	
