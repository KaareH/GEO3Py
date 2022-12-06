# GEO3, Python port
# FStTrunc
# functions/FStTrunc.py


# Description:
No description provided
#
# Globals: 
# Locals:  rP, fst
# Parameters: r, L
def FStTrunc(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	rP:= unapply(convert(diff(r(t),t), D),t)
	fst:= unapply(rP(t)/(0.0001+nrm(rP(t))), t)
	convert(evalm(fst(L[1])), list)
	
##################################
########## ORIGINAL ##############
##################################
	
	rP:= unapply(convert(diff(r(t),t), D),t);
	fst:= unapply(rP(t)/(0.0001+nrm(rP(t))), t);
	convert(evalm(fst(L[1])), list);
	
