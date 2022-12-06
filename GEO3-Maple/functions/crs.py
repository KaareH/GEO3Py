# GEO3, Python port
# crs
# functions/crs.py


# Description:
No description provided
#
# Globals: 
# Locals:  a,b,c
# Parameters: X,Y
def crs(X, Y):
	##################################
	########## CONVERTED #############
	##################################
	
	a := X[2]*Y[3]-X[3]*Y[2]
	b := X[3]*Y[1]-X[1]*Y[3]
	c := X[1]*Y[2]-X[2]*Y[1]
	convert(evalm(simplify([a,b,c])), list)
	
##################################
########## ORIGINAL ##############
##################################
	    
	    a := X[2]*Y[3]-X[3]*Y[2];
	    b := X[3]*Y[1]-X[1]*Y[3];
	    c := X[1]*Y[2]-X[2]*Y[1];
	    convert(evalm(simplify([a,b,c])), list);
	
