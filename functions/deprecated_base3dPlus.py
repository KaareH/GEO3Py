# GEO3, Python port
# deprecated_base3dPlus
# functions/deprecated_base3dPlus.py


# 3d base plot translated and rotated and colored
# Globals: 
# Locals:  e1_3d, mark1_3d, e2_3d, mark2_3d, e3_3d, mark3_3d, i
# Parameters: x,y,z, trans, rot, col
def deprecated_base3dPlus(x,y,z, trans, rot, col):
	
	
	
	e1_3d:= arrow(trans, evalm((rot&*[1,0,0])),  0.05, 0.1, 0.1,shape=cylindrical_arrow, fringe = 'black', color=col):
	e2_3d:= arrow(trans, evalm((rot&*[0,1,0])),  0.05, 0.1, 0.1,shape=cylindrical_arrow, fringe = 'black', color=col):
	e3_3d:= arrow(trans, evalm((rot&*[0,0,1])),  0.05, 0.1, 0.1,shape=cylindrical_arrow, fringe = 'black', color=col):
	mark1_3d:= x-> textplot3d([seq(evalm(trans+(rot&*[1.2,0,0]))[i], i=1..3),`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_3d:= y-> textplot3d([seq(evalm(trans+(rot&*[0,1.2,0]))[i], i=1..3),`y`],
	color=black, font=[TIMES, ITALIC, 20]):
	mark3_3d:= z-> textplot3d([seq(evalm(trans+(rot&*[0,0,1.2]))[i], i=1..3),`z`], 
	color=black, font=[TIMES, ITALIC, 20]):
	display([e1_3d, mark1_3d(x), e2_3d, mark2_3d(y), e3_3d, mark3_3d(z)], lightmodel=light4, scaling=constrained):
	
