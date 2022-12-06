# GEO3, Python port
# FSb
# functions/FSb.py


# Description:
No description provided
#
# Globals: 
# Locals:  rP, rPP, cr, fsb
# Parameters: r, L
def FSb(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	rP:=  unapply(convert(diff(r(t),t), D),t)
	rPP:= unapply(convert(diff(rP(t),t), D),t)
	cr:=  unapply(crs(rP(t), rPP(t)),t)
	fsb:= unapply(simplify(cr(t)/nrm(cr(t))), t)
	convert(evalm(fsb(L[1])),list)
	
##################################
########## ORIGINAL ##############
##################################
	
	rP:=  unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D),t);
	cr:=  unapply(crs(rP(t), rPP(t)),t);
	fsb:= unapply(simplify(cr(t)/nrm(cr(t))), t);
	convert(evalm(fsb(L[1])),list);
	
