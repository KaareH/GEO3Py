# GEO3, Python port
# evoluteTrunc
# functions/evoluteTrunc.py


# Description:
# Finds (display version, truncated) evolute vector function from given
# parametrization of non-null curved curve, arc-length param or not.
#
# Globals: 
# Locals:  ev
# Parameters: r, L
def evoluteTrunc(r, L):
	
	
	 
	ev:= unapply(simplify(r(t) + (1/(0.0000001+kappaTrunc(r, [t])))*FSnTrunc(r, [t])), t);
	convert(evalm(ev(L[1])), list);
	
