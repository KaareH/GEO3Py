# GEO3, Python port
# deprecated_base2d
# functions/deprecated_base2d.py


# Description:
# 2d basis plot
#
# Globals: 
# Locals:  e1_2d,mark1_2d, e2_2d, mark2_2d, axlong1, axlong2
# Parameters: x,y
def deprecated_base2d(x, y):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	e1_2d:= arrow(<1, 0>, color=red):
	e2_2d:= arrow(<0, 1>, color=blue):
	mark1_2d:= x-> textplot([1.2, -0.2,`x`],
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_2d:= y-> textplot([-0.2, 1.2,`y`],
	color=black, font=[TIMES, ITALIC, 20]):
	axlong1:= plot([u,0, u=-0.5...1.5], color=black)
	axlong2:= plot([0,u, u=-0.5...1.5], color=black)
	display([e1_2d, mark1_2d(x), e2_2d, mark2_2d(y), axlong1, axlong2],
	scaling=constrained, axes=none):
	
##################################
########## ORIGINAL ##############
##################################
	
	
	
	e1_2d:= arrow(<1, 0>, color=red):
	e2_2d:= arrow(<0, 1>, color=blue):
	mark1_2d:= x-> textplot([1.2, -0.2,`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_2d:= y-> textplot([-0.2, 1.2,`y`], 
	color=black, font=[TIMES, ITALIC, 20]):
	axlong1:= plot([u,0, u=-0.5...1.5], color=black);
	axlong2:= plot([0,u, u=-0.5...1.5], color=black);
	display([e1_2d, mark1_2d(x), e2_2d, mark2_2d(y), axlong1, axlong2], 
	scaling=constrained, axes=none):
	
