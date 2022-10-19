# GEO3, Python port
# FSn
# functions/FSn.py


# 
# Globals: 
# Locals:  fsn
# Parameters: r, L
def FSn(r, L):
	 
	fsn:= unapply(simplify(crs(FSb(r, [t]), FSt(r, [t]))),t);
	convert(evalm(fsn(L[1])), list);
	
