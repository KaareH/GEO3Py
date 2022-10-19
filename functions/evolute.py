# GEO3, Python port
# evolute
# functions/evolute.py


# Finds evolute vector function from given
parametrization of non-null curved curve, arc-length param or not.
# Globals: 
# Locals:  ev
# Parameters: r, L
def evolute(r, L):
	
	
	 
	ev:= unapply(simplify(r(t) + (1/kappa(r, [t]))*FSn(r, [t])), t);
	convert(evalm(ev(L[1])), list);
	
