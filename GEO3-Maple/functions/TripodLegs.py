# GEO3, Python port
# TripodLegs
# functions/TripodLegs.py


# Description:
# Tripod 3 legs display with marked orientations
#
# Globals: 
# Locals:  col, pt, ara, arb, ac, linab, linac, linbc
# Parameters: p::list, a::list, b::list, c::list
def TripodLegs(p, a, b, c):
	##################################
	########## CONVERTED #############
	##################################
	
	
	###########################################################
	
	###########################################################
	
	
	linab:= line(p+a, p+b, color=black)
	linac:= line(p+a, p+c, color=black)
	linbc:= line(p+b, p+c, color=black)
	
	
	pt:= sphere(p, 0.07, color=yellow, style=patchnogrid)
	
	ara:= display(arrow(Vector(p), Vector(a), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=black))
	
	arb:= display(arrow(Vector(p), Vector(b), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color="Chocolate"))
	
	ac:= display(arrow(Vector(p), Vector(c), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=gray))
	
	
	display(pt, ara, arb, ac, linab, linac, linbc, scaling=constrained, axes=none, projection=0.8)
	
	#############################################################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	###########################################################
	
	###########################################################
	
	
	linab:= line(p+a, p+b, color=black);
	linac:= line(p+a, p+c, color=black);
	linbc:= line(p+b, p+c, color=black);
	
	
	pt:= sphere(p, 0.07, color=yellow, style=patchnogrid);
	
	ara:= display(arrow(Vector(p), Vector(a), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=black));
	
	arb:= display(arrow(Vector(p), Vector(b), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color="Chocolate"));
	
	ac:= display(arrow(Vector(p), Vector(c), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=gray));
	
	
	display(pt, ara, arb, ac, linab, linac, linbc, scaling=constrained, axes=none, projection=0.8);
	
	#############################################################
	
