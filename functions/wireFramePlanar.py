# GEO3, Python port
# wireFramePlanar
# functions/wireFramePlanar.py


# Description:
# Wireframe model of planar domain.
#
# Globals: 
# Locals:  
          q, p, Delta,x, y,  ku, kv, sys
# Parameters: r, B, net
def wireFramePlanar(r, B, net):
	
	
	          
	Delta[1]:= evalf((B[2]-B[1])/net[1]);
	Delta[2]:= evalf((B[4]-B[3])/net[2]);
	
	
	x:= (u,v)-> r(u,v)[1];
	y:= (u,v)-> r(u,v)[2];
	
	ku:= v -> plot([x(u,v), y(u,v), u=B[1]...B[2]], color=red):
	kv:= u -> plot([x(u,v), y(u,v), v=B[3]...B[4]], color=blue):
	sys[1]:= display(seq(ku(B[3]+q*Delta[2]), q=0...net[2])):
	sys[2]:= display(seq(kv(B[1]+p*Delta[1]), p=0...net[1])):
	display([sys[1], sys[2]]):
	
	
