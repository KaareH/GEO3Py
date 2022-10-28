# GEO3, Python port
# Base3dRot
# functions/Base3dRot.py


# Description:
# Rotated by A 3d base at p plot with axes of explicit length specification in list len
#
# Globals: 
# Locals:  e1_3d, mark1_3d, e2_3d, e3_3d,lin1, lin2, lin3, 
axlong1, axlong2, axlong3, Nlen, a1, a2, a3, m1, m2, m3
# Parameters: p::list, A::Matrix, x,y,z, len::list
def Base3dRot(p, A, x, y, z, len):
	
	
	####################
	
	####################
	
	if nargs=5 then 
	Nlen:= [0, 1.5, 0,1.5, 0,1.5] 
	else Nlen:= len end if;
	
	
	
	
	
	
	a1:= convert(A.Vector([1.2,0,-0.1]), list);
	a2:= convert(A.Vector([0, 1.2,0.1]), list);
	a3:= convert(A.Vector([-0.1, 0, 1.2]), list);
	
	
	
	m1:= textplot3d([op(a1+p),`x`], 
	color=black, font=[TIMES, ITALIC, 20]):
	m2:= textplot3d([op(a2+p),`y`], 
	color=black, font=[TIMES, ITALIC, 20]):
	m3:= textplot3d([op(a3+p),`z`], 
	color=black, font=[TIMES, ITALIC, 20]):
	
	
	
	
	
	
	
	
	e1_3d:= arrow(<op(p)>, A.<1,0,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="PaleVioletRed"):
	e2_3d:= arrow(<op(p)>, A.<0,1,0>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="SlateBlue"):
	e3_3d:= arrow(<op(p)>, A.<0,0,1>, 0.05, 0.1, 0.1, cylindrical_arrow, fringe = 'black', color="SpringGreen"):
	
	lin1:= u-> convert(evalm(p+u*[A[1,1], A[2,1], A[3,1]]), list);
	lin2:= u-> convert(evalm(p+u*[A[1,2], A[2,2], A[3,2]]), list);
	lin3:= u-> convert(evalm(p+u*[A[1,3], A[2,3], A[3,3]]), list);
	
	
	
	axlong1:= spacecurve([op(lin1(u)), u=Nlen[1]...Nlen[2]], color=black); #Axes lengths
	axlong2:= spacecurve([op(lin2(u)), u=Nlen[3]...Nlen[4]], color=black);
	axlong3:= spacecurve([op(lin3(u)), u=Nlen[5]...Nlen[6]], color=black);
	display(
	[m1, m2, m3, axlong1, axlong2, axlong3, e1_3d,  e2_3d, e3_3d], 
	lightmodel=light4, scaling=constrained, projection=0.8):
	
	####################
	# Result: 
	if nargs=5 then 
	Nlen:= [0, 1.5, 0,1.5, 0,1.5] 
	else Nlen:= len end if
	# Result: 
	 nargs=5 
	# Result: 
	 
	Nlen:= [0, 1.5, 0,1.5, 0,1.5] 
	
	# Result: 
	 Nlen:= len 
	
