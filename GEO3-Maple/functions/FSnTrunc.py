# GEO3, Python port
# FSnTrunc
# functions/FSnTrunc.py


# Description:
No description provided
#
# Globals: 
# Locals:  fsn
# Parameters: r, L
def FSnTrunc(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	fsn:= unapply(evalf(crs(FSbTrunc(r, [t]), FStTrunc(r, [t]))),t)
	convert(evalm(fsn(L[1])), list)
	
##################################
########## ORIGINAL ##############
##################################
	 
	fsn:= unapply(evalf(crs(FSbTrunc(r, [t]), FStTrunc(r, [t]))),t);
	convert(evalm(fsn(L[1])), list);
	
