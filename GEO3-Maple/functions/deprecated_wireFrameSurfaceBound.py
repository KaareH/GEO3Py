# GEO3, Python port
# deprecated_wireFrameSurfaceBound
# functions/deprecated_wireFrameSurfaceBound.py


# Description:
# Wireframe model of surface with boundary
#
# Globals: 
# Locals:  
     q, p, i, Delta, rr, ku, kv, sys, deform, kurve, kurveTotal, flade, paramC
# Parameters: r, B, net, gamU, BgamU
def deprecated_wireFrameSurfaceBound(r, B, net, gamU, BgamU):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	
	Delta[1]:= evalf((B[2]-B[1])/net[1])
	Delta[2]:= evalf((B[4]-B[3])/net[2])
	
	rr[1]:= u-> r(u, B[3])
	rr[2]:= v-> r(B[2], v)
	rr[3]:= u-> r(B[2]- u, B[4])
	rr[4]:= v-> r(B[1], B[4] - v)
	
	ku:= v -> spacecurve(r(u,v), u=B[1]...B[2],
	color=red):
	kv:= u -> spacecurve(r(u,v), v=B[3]...B[4],
	color=blue):
	
	sys[1]:= display(seq(ku(B[3]+q*Delta[2]), q=0...net[2])):
	sys[2]:= display(seq(kv(B[1]+p*Delta[1]), p=0...net[1])):
	
	deform:= display([sys[1], sys[2]],
	scaling=constrained, projection=0.8):
	flade:= plot3d(r(u,v), u=B[1]...B[2], v=B[3]...B[4],
	grid=[3*net[1], 3*net[2]], scaling=constrained):
	
	kurve[1]:= spacecurve(rr[1](u), u=B[1]...B[2], thickness=2, color=green):
	kurve[2]:= spacecurve(rr[2](v), v=B[3]...B[4], thickness=2, color=green):
	kurve[3]:= spacecurve(rr[3](u), u=0...B[2]-B[1],thickness=2, color=green):
	kurve[4]:= spacecurve(rr[4](v), v=0...B[4]-B[3],  thickness=2, color=green):
	
	kurveTotal:= display(seq(kurve[i], i=1...4)):
	
	if nargs > 3 :
		paramC:= spacecurve(r(gamU(t)[1], gamU(t)[2]), t=BgamU[1]...BgamU[2], color=black, thickness=2)
	else:
		paramC:= NULL
	
	
	display([deform, kurveTotal, base3d(x,y,z), paramC],
	scaling=constrained, projection=0.8)
	
	
##################################
########## ORIGINAL ##############
##################################
	
	
	          
	
	Delta[1]:= evalf((B[2]-B[1])/net[1]);
	Delta[2]:= evalf((B[4]-B[3])/net[2]);
	
	rr[1]:= u-> r(u, B[3]);
	rr[2]:= v-> r(B[2], v);
	rr[3]:= u-> r(B[2]- u, B[4]);
	rr[4]:= v-> r(B[1], B[4] - v);
	
	  ku:= v -> spacecurve(r(u,v), u=B[1]...B[2], 
	            color=red):
	  kv:= u -> spacecurve(r(u,v), v=B[3]...B[4], 
	            color=blue):  
	
	  sys[1]:= display(seq(ku(B[3]+q*Delta[2]), q=0...net[2])):  
	  sys[2]:= display(seq(kv(B[1]+p*Delta[1]), p=0...net[1])):
	
	  deform:= display([sys[1], sys[2]], 
	           scaling=constrained, projection=0.8):
	  flade:= plot3d(r(u,v), u=B[1]...B[2], v=B[3]...B[4], 
	          grid=[3*net[1], 3*net[2]], scaling=constrained):
	
	kurve[1]:= spacecurve(rr[1](u), u=B[1]...B[2], thickness=2, color=green):
	kurve[2]:= spacecurve(rr[2](v), v=B[3]...B[4], thickness=2, color=green):
	kurve[3]:= spacecurve(rr[3](u), u=0...B[2]-B[1],thickness=2, color=green):
	kurve[4]:= spacecurve(rr[4](v), v=0...B[4]-B[3],  thickness=2, color=green):
	
	kurveTotal:= display(seq(kurve[i], i=1...4)):
	
	if nargs > 3 then 
	paramC:= spacecurve(r(gamU(t)[1], gamU(t)[2]), t=BgamU[1]...BgamU[2], color=black, thickness=2);
	else
	paramC:= NULL;
	end if;
	
	display([deform, kurveTotal, base3d(x,y,z), paramC], 
	scaling=constrained, projection=0.8);
	
	
