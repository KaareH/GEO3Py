# GEO3, Python port
# Base3dFixAll
# functions/Base3dFixAll.py


# 3d New Fixed base plot with axes of explicit length specification in list len
# Globals: 
# Locals:  e1_3d, mark1_3d, e2_3d, mark2_3d, e3_3d, mark3_3d, 
axlong1, axlong2, axlong3, Nlen, markOrigo, marke1, marke2, marke3
# Parameters: x,y,z, len
def Base3dFixAll(x,y,z, len):
	
	
	####################
	
	####################
	
	if nargs=3 then 
	Nlen:= [0, 1.5, 0,1.5, 0,1.5] 
	else Nlen:= len end if;
	
	
	e1_3d:= arrow(<0,0,0>, <1,0,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="PaleVioletRed"):
	e2_3d:= arrow(<0,0,0>, <0,1,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="SlateBlue"):
	e3_3d:= arrow(<0,0,0>, <0,0,1>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="SpringGreen"):
	mark1_3d:= x-> textplot3d([1.2, 0, -0.1,`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark2_3d:= y-> textplot3d([0, 1.2, 0.1,`y`], 
	color=black, font=[TIMES, ITALIC, 20]):
	mark3_3d:= z-> textplot3d([-0.1, 0, 1.2,`z`], 
	color=black, font=[TIMES, ITALIC, 20]):
	
	
	markOrigo:= textplot3d([-0.0, -0.15, 0.1, `Q`], 
	color=black, font=[TIMES, ITALIC, 20]):
	marke1:= textplot3d([0.5, 0.1, -0.1, 'e'], 
	color=black, font=[TIMES, BOLDITALIC, 25]):
	marke2:= textplot3d([0.1, 0.5, -0.1, `f`], 
	color=black, font=[TIMES, BOLDITALIC, 25]):
	marke3:= textplot3d([-0.1, 0.1, 0.5, `g`], 
	color=black, font=[TIMES, BOLDITALIC, 25]):
	
	
	
	
	axlong1:= spacecurve([u,0,0, u=Nlen[1]...Nlen[2]], color=black); #Axes lengths
	axlong2:= spacecurve([0,u,0, u=Nlen[3]...Nlen[4]], color=black);
	axlong3:= spacecurve([0,0,u, u=Nlen[5]...Nlen[6]], color=black);
	display(
	[axlong1, axlong2, axlong3, e1_3d, mark1_3d(x), e2_3d, mark2_3d(y), e3_3d, mark3_3d(z), markOrigo, marke1, marke2, marke3], 
	lightmodel=light4, scaling=constrained, projection=0.8):
	
	####################
	
