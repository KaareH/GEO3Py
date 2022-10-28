# GEO3, Python port
# FSt
# functions/FSt.py


# Description:
No description provided
#
# Globals: 
# Locals:  rP, fst
# Parameters: r, L
def FSt(r, L):
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	fst:= unapply(simplify(rP(t)/nrm(rP(t))), t);
	convert(evalm(fst(L[1])), list);
	
