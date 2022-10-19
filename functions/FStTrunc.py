# GEO3, Python port
# FStTrunc
# functions/FStTrunc.py


# 
# Globals: 
# Locals:  rP, fst
# Parameters: r, L
def FStTrunc(r, L):
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	fst:= unapply(rP(t)/(0.0001+nrm(rP(t))), t);
	convert(evalm(fst(L[1])), list);
	
