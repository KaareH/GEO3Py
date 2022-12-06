# GEO3, Python port
# deprecated_ParamDomain
# functions/deprecated_ParamDomain.py


# Description:
# Shows the 2D-parameter domain.
#
# Globals: 
# Locals:  q, p, x, y, kuT, kvT, sysT, Delta, paramC
# Parameters: BB, netnet
def deprecated_ParamDomain(BB, netnet):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	
	Delta[1]:= evalf((BB[2]-BB[1])/netnet[1])
	Delta[2]:= evalf((BB[4]-BB[3])/netnet[2])
	
	x:= (u,v)-> u
	y:= (u,v)-> v
	kuT:= v -> plot([u, v, u=BB[1]...BB[2]], color=red):
	kvT:= u -> plot([u, v, v=BB[3]...BB[4]], color=blue)
	
	sysT[1]:= display(seq(kuT(BB[3]+q*Delta[2]), q=0...netnet[2])):
	sysT[2]:= display(seq(kvT(BB[1]+p*Delta[1]), p=0...netnet[1])):
	
	display([base2d(u,v), sysT[1], sysT[2]],
	scaling=constrained, tickmarks=[2,2])
	
	
##################################
########## ORIGINAL ##############
##################################
	
	
	   
	
	Delta[1]:= evalf((BB[2]-BB[1])/netnet[1]);
	Delta[2]:= evalf((BB[4]-BB[3])/netnet[2]);
	
	x:= (u,v)-> u;
	y:= (u,v)-> v;
	kuT:= v -> plot([u, v, u=BB[1]...BB[2]], color=red):
	kvT:= u -> plot([u, v, v=BB[3]...BB[4]], color=blue);
	
	sysT[1]:= display(seq(kuT(BB[3]+q*Delta[2]), q=0...netnet[2])):
	sysT[2]:= display(seq(kvT(BB[1]+p*Delta[1]), p=0...netnet[1])):
	
	display([base2d(u,v), sysT[1], sysT[2]], 
	scaling=constrained, tickmarks=[2,2]);
	
	
