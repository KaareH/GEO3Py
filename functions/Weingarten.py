# GEO3, Python port
# Weingarten
# functions/Weingarten.py


# Description:
# Calculates the Weingarten matrix from given 
# parametrization r. Out parameters or values are specified in given 2-element list L
#
# Globals: 
# Locals:  wein
# Parameters: r, L
def Weingarten(r, L):
	
	
	      
	#####################################################################
	      wein:= (u,v)-> evalm(MatrixInverse(FI(r,[u,v]))&*FII(r, [u,v]));
	      Matrix(2,2, wein(L[1], L[2]));
	
