# GEO3, Python port
# Tripod
# functions/Tripod.py


# Description:
# ThreeLeg display with marked orientations and tetrahedron
#
# Globals: 
# Locals:  col, mat, pt, ara, arb, ac, faceab, faceac, facebc, faceabc, faceAll
# Parameters: p::list, a::list, b::list, c::list
def Tripod(p, a, b, c):
	##################################
	########## CONVERTED #############
	##################################
	
	
	###########################################################
	
	###########################################################
	
	
	mat:= Transpose(Matrix([a, b, c]));
	
	
	if evalf(Determinant(mat))>=0 : col:=cyan
	else:
		
	
	
	
	
	
	pt:= sphere(p, 0.07, color=yellow, style=patchnogrid)
	
	ara:= display(arrow(Vector(p), Vector(a), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=black))
	
	arb:= display(arrow(Vector(p), Vector(b), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color="Chocolate"))
	
	ac:= display(arrow(Vector(p), Vector(c), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=gray))
	
	
	faceab:=  polygonplot3d([p, a+p, b+p],   color = col)
	faceac:=  polygonplot3d([p, a+p, c+p],   color = col)
	facebc:=  polygonplot3d([p, b+p, c+p],   color = col)
	faceabc:= polygonplot3d([a+p, b+p, c+p], color = col)
	
	faceAll:= display(faceab, faceac, facebc, faceabc)
	
	display(pt, ara, arb, ac, faceAll, scaling=constrained, axes=none, projection=0.8)
	
	#############################################################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	###########################################################
	
	###########################################################
	
	
	mat:= Transpose(Matrix([a, b, c])); 
	
	if evalf(Determinant(mat))>=0 then col:=cyan 
	else col:=khaki; 
	end if;
	
	
	
	
	pt:= sphere(p, 0.07, color=yellow, style=patchnogrid);
	
	ara:= display(arrow(Vector(p), Vector(a), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=black));
	
	arb:= display(arrow(Vector(p), Vector(b), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color="Chocolate"));
	
	ac:= display(arrow(Vector(p), Vector(c), 0.06, 0.12, 0.12,  cylindrical_arrow, fringe=red, color=gray));
	
	
	faceab:=  polygonplot3d([p, a+p, b+p],   color = col);
	faceac:=  polygonplot3d([p, a+p, c+p],   color = col);
	facebc:=  polygonplot3d([p, b+p, c+p],   color = col);
	faceabc:= polygonplot3d([a+p, b+p, c+p], color = col);
	
	faceAll:= display(faceab, faceac, facebc, faceabc);
	
	display(pt, ara, arb, ac, faceAll, scaling=constrained, axes=none, projection=0.8);
	
	#############################################################
	
