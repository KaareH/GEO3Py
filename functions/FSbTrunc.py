# GEO3, Python port
# FSbTrunc
# functions/FSbTrunc.py


# Description:
No description provided
#
# Globals: 
# Locals:  rP, rPP, cr, fsb
# Parameters: r, L
def FSbTrunc(r, L):
	
	rP:=  unapply(convert(diff(r(t),t), D),t);
	rPP:= unapply(convert(diff(rP(t),t), D),t);
	cr:=  unapply(crs(rP(t), rPP(t)),t);
	fsb:= unapply(evalf(cr(t)/(0.0001+nrm(cr(t)))), t);
	convert(evalm(fsb(L[1])),list);
	
