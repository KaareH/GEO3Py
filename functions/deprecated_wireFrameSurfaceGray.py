# GEO3, Python port
# deprecated_wireFrameSurfaceGray
# functions/deprecated_wireFrameSurfaceGray.py


# Wireframe model of surface - in gray.
# Globals: 
# Locals:  
          q, p, Delta, ku, kv, sys, paramC
# Parameters: r, B, net, gamU, BgamU
def deprecated_wireFrameSurfaceGray(r, B, net, gamU, BgamU):
	
	
	          
	
	  Delta[1]:= evalf((B[2]-B[1])/net[1]);
	  Delta[2]:= evalf((B[4]-B[3])/net[2]);
	
	  ku:= v -> spacecurve(r(u,v), u=B[1]...B[2], 
	            color=gray):
	  kv:= u -> spacecurve(r(u,v), v=B[3]...B[4], 
	            color=gray):  
	  sys[1]:= display(seq(ku(B[3]+q*Delta[2]), q=0...net[2])):  
	  sys[2]:= display(seq(kv(B[1]+p*Delta[1]), p=0...net[1])): 
	 
	if nargs > 3 then 
	paramC:= spacecurve(r(gamU(t)[1], gamU(t)[2]), t=BgamU[1]...BgamU[2], color=black, thickness=2);
	else
	paramC:= NULL;
	end if;
	
	
	  display([base3d(x,y,z), sys[1], sys[2], paramC], 
	           scaling=constrained, projection=0.8):
	
	
