# GEO3, Python port
# Base3d
# functions/Base3d.py


# 3d base plot with axes of explicit length specification in list len
# Globals: 
# Locals:  e1_3d, mark1_3d, e2_3d, mark2_3d, e3_3d, mark3_3d, 
axlong1, axlong2, axlong3, Nlen, Nsiz
# Parameters: x,y,z, len, siz
def Base3d(x,y,z, len, siz):
	
	
	####################
	
	####################
	
	if nargs=3 then 
	Nsiz:= 20; Nlen:= [0, 1.5, 0,1.5, 0,1.5] 
	else end if;
	
	if nargs=4 then 
	Nsiz:= 20; Nlen:= len; else end if;
	
	if nargs=5 then 
	Nsiz:= siz; Nlen:= len; else end if;
	
	e1_3d:= arrow(<0,0,0>, <1,0,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=red):
	e2_3d:= arrow(<0,0,0>, <0,1,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=blue):
	e3_3d:= arrow(<0,0,0>, <0,0,1>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color=green):
	mark1_3d:= x-> textplot3d([1.2, 0, -0.1,`x`], 
	color=black, font=[TIMES, ITALIC, Nsiz]):
	mark2_3d:= y-> textplot3d([0, 1.2, 0.1,`y`], 
	color=black, font=[TIMES, ITALIC, Nsiz]):
	mark3_3d:= z-> textplot3d([-0.1, 0, 1.2,`z`], 
	color=black, font=[TIMES, ITALIC, Nsiz]):
	axlong1:= spacecurve([u,0,0, u=Nlen[1]...Nlen[2]], color=black); #Axes lengths
	axlong2:= spacecurve([0,u,0, u=Nlen[3]...Nlen[4]], color=black);
	axlong3:= spacecurve([0,0,u, u=Nlen[5]...Nlen[6]], color=black);
	display(
	[axlong1, axlong2, axlong3, e1_3d, mark1_3d(x), e2_3d, mark2_3d(y), e3_3d, mark3_3d(z)], 
	lightmodel=light4, scaling=constrained, projection=0.8):
	
	####################
	
