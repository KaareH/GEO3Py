# GEO3, Python port
# FInrm
# functions/FInrm.py


# Calculates the length of vector v with given coordinates [uP, vP] w.r.t. 
standard coordinate basis at parameter point (L[1], L[2]) from given 
parametrization r. Out parameters or values are as specified in 2-element list L
# Globals: 
# Locals:  rP1,rP2, u,v, E, F, G, len
# Parameters: r, vec, L
def FInrm(r, vec, L):
	
	
	      
	      rP1 := unapply(convert(diff(r(u,v), u),D), u,v):
	      rP2 := unapply(convert(diff(r(u,v), v),D), u,v):
	      E:= unapply(dot(rP1(u,v),rP1(u,v)), u,v):
	      F:= unapply(dot(rP1(u,v),rP2(u,v)), u,v):
	      G:= unapply(dot(rP2(u,v),rP2(u,v)), u,v):
	len:= (u,v)-> sqrt(simplify((vec[1]^2)*E(u,v) + 2*vec[1]*vec[2]*F(u,v) + (vec[2]^2)*G(u,v)));
	len(L[1], L[2]);
	
