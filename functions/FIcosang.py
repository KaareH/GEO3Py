# GEO3, Python port
# FIcosang
# functions/FIcosang.py


# Calculates COSINE OF the angle between vectors v and w at parameter point (L[1], L[2]) from given 
parametrization r. Out parameters or values are as specified in 2-element list L
# Globals: 
# Locals:  rP1,rP2, u,v, E, F, G, ang
# Parameters: r, vec1, vec2, L
def FIcosang(r, vec1, vec2, L):
	
	
	      
	ang:= (u,v)-> simplify(FIdot(r, vec1, vec2, [u,v])/sqrt(FIdot(r, vec1, vec1, [u,v])*FIdot(r, vec2, vec2, [u,v])));
	ang(L[1], L[2]);
	
