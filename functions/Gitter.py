# GEO3, Python port
# Gitter
# functions/Gitter.py


# Viser traadmodel af rumlige omraade  r(B), hvor B er 3d og tidsafhængig.
# Globals: 
# Locals:  u,v,w,x,y,z,tt, q, p,
          Delta, ku, kv, kw, sys, r
# Parameters: rr, t, B, net
def Gitter(rr, t, B, net):
	
	
	          
	
	############################################################################
	#map(assume, [u,v,w,t,x,y,z], real);
	#assume(u>=B[1], u<=B[2], v>=B[3], v<=B[4], w>=B[5], w<=B[6]);
	#################################################
	r:= unapply(convert(rr(u,v,w,tt),list), u,v,w,tt);
	#################################################
	
	Delta[1]:= evalf((B[2]-B[1])/net[1]);
	Delta[2]:= evalf((B[4]-B[3])/net[2]);
	Delta[3]:= evalf((B[6]-B[5])/net[3]);
	
	ku:= (v,w) -> spacecurve(r(u,v,w,t), u=B[1]...B[2], 
	color=black):
	kv:= (u,w) -> spacecurve(r(u,v,w,t), v=B[3]...B[4], 
	color=black):
	kw:= (u,v) -> spacecurve(r(u,v,w,t), w=B[5]...B[6], 
	color=black):
	sys[1]:= display(
	seq(seq(
	ku(B[3]+q*Delta[2], B[5]+tt*Delta[3]), q=0...net[2]), tt=0...net[3])):
	sys[2]:= display(
	seq(seq(
	kv(B[1]+p*Delta[1], B[5]+tt*Delta[3]), p=0...net[1]), tt=0...net[3])):
	sys[3]:= display[plots](
	seq(seq(
	kw(B[1]+p*Delta[1], B[3]+q*Delta[2]), p=0...net[1]), q=0...net[2])):
	
	display([sys[1], sys[2], sys[3]], scaling=constrained, projection=0.8, axes=none):
	
	
