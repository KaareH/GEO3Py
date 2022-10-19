# GEO3, Python port
# Base2d
# functions/Base2d.py


# 2d basis plot
# Globals: 
# Locals:  e1_2d,mark1_2d, e2_2d, mark2_2d, axlong1, axlong2, Nlen
# Parameters: x,y, len
def Base2d(x,y, len):
	
	
	###########################################################
	
	###########################################################
	if nargs=2 then 
	Nlen:= [0, 1.5, 0,1.5] 
	else Nlen:= len end if;
	
	e1_2d:= arrow([0,0], [1,0], 0.05, 0.10, 0.15,  color=red):
	e2_2d:= arrow([0,0], [0,1], 0.05, 0.10, 0.15,  color=blue):
	mark1_2d:= x-> textplot([1.2, -0.2,`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_2d:= y-> textplot([-0.2, 1.2,`y`], 
	color=black, font=[TIMES, ITALIC, 20]):
	axlong1:= plot([u,0, u=Nlen[1]...Nlen[2]], color=black);
	axlong2:= plot([0,u, u=Nlen[3]...Nlen[4]], color=black);
	display([e1_2d, mark1_2d(x), e2_2d, mark2_2d(y), axlong1, axlong2], 
	scaling=constrained, axes=none):
	###########################################################
	
