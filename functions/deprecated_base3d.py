# GEO3, Python port
# deprecated_base3d
# functions/deprecated_base3d.py


# Description:
# 3d base plot
#
# Globals: 
# Locals:  e1_3d, mark1_3d, e2_3d, mark2_3d, e3_3d, mark3_3d,
axlong1, axlong2, axlong3
# Parameters: x,y,z, len::list:=[-0.5, 1.5, -0.5, 1.5, -0.5, 1.5]
def deprecated_base3d(x, y, z, len, 1.5, -0.5, 1.5, -0.5, 1.5]):
	
	
	
	e1_3d:= arrow(<0,0,0>, <1,0,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=red):
	e2_3d:= arrow(<0,0,0>, <0,1,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=blue):
	e3_3d:= arrow(<0,0,0>, <0,0,1>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=green):
	mark1_3d:= x-> textplot3d([1.2, -0.2, -0.2,`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_3d:= y-> textplot3d([-0.2, 1.2, -0.2,`y`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark3_3d:= z-> textplot3d([0.2, 0.2, 1.2,`z`], 
	color=black, font=[TIMES, ITALIC, 20]):
	axlong1:= spacecurve([u,0,0, u=len[1]...len[2]], color=black);
	axlong2:= spacecurve([0,u,0, u=len[3]...len[4]], color=black);
	axlong3:= spacecurve([0,0,u, u=len[5]...len[6]], color=black);
	display(
	[axlong1, axlong2, axlong3, e1_3d, mark1_3d(x), e2_3d, mark2_3d(y), e3_3d, mark3_3d(z)], 
	lightmodel=light4, scaling=constrained, projection=0.8):
	
