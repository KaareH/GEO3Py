# GEO3, Python port
# FSn
# functions/FSn.py


# Description:
No description provided
#
# Globals: 
# Locals:  fsn
# Parameters: r, L
def FSn(r, L):
	##################################
	########## CONVERTED #############
	##################################
	
	fsn:= unapply(simplify(crs(FSb(r, [t]), FSt(r, [t]))),t)
	convert(evalm(fsn(L[1])), list)
	
##################################
########## ORIGINAL ##############
##################################
	 
	fsn:= unapply(simplify(crs(FSb(r, [t]), FSt(r, [t]))),t);
	convert(evalm(fsn(L[1])), list);
	
