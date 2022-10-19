# GEO3, Python port
# Hinge
# functions/Hinge.py


# Hinge display with marked orientation.
# Globals: 
# Locals:  col, mat, pt, ara, arb, faceab
# Parameters: p::list, a::list, b::list
def Hinge(p::list, a::list, b::list):
	
	
	###########################################################
	
	###########################################################
	
	##########
	if nops(a)=2 then
	##########
	
	mat:= Transpose(Matrix([a, b])); 
	
	if evalf(Determinant(mat))>=0 then col:=cyan 
	else col:=khaki; 
	end if;
	
	pt:= disk(p, 0.07, color=yellow);
	
	ara:= display(arrow(p, a+p, 0.08, 0.16, 0.16,  color=black));
	
	arb:= display(arrow(p, b+p, 0.08, 0.16, 0.16,  color=gray));
	
	display(pt, polygon([p, a+p, b+p], color = col,  thickness = 1), ara, arb, scaling=constrained, axes=none);
	##########
	else
	##########
	pt:= sphere(p, 0.07, color=yellow, style=patchnogrid);
	
	ara:= display(arrow(Vector(p), Vector(a), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=black));
	
	arb:= display(arrow(Vector(p), Vector(b), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=gray));
	
	faceab:=  polygonplot3d([p, a+p, b+p],   color = cyan);
	
	
	
	display(pt, ara, arb, faceab, scaling=constrained, axes=none, projection=0.8);
	
	
	##########
	end if;
	##########
	
	
	#############################################################
	
