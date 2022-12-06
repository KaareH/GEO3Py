# GEO3, Python port
# deprecated_SurfDraw
# functions/deprecated_SurfDraw.py


# Description:
# Dynamic drawing of a given surface: 
# Four boundary curves and a number of coordiante curves according 
# to net-specifications.
#
# Globals: 
# Locals:  
q, p, i, anim, animu1, animu2, animv1, animv2, net, questn, Af,Delta, questr, questB, kurveu1, kurveu2, kurvev1, kurvev2,  maksval, extension, maxi, mini, hs, n, randkurv,
bd, ku, kv, sys, deform, filling, m, j, coordu, coordv, ko, animko, k, w, animkou, qq, animfull, qqq, animfullT, animfullu, stillu, ww, mm, fullu, fullv, questf, minf, maxf, poly, fyld,
brick, bb, kou, kov, animkov, animBdNet, br, bricklay
# Parameters: r, B, netraw
def deprecated_SurfDraw(r, B, netraw):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	
	##################################################
	
	if nargs=3 :
		net:= netraw
		if
		type(net[1], numeric) and type(net[2], numeric) then
		questn:=true else questn:=false
		net:= [5,5] end if
	else:
		net:=[5,5] end if
		
		questB:= type(evalf(B[1]), numeric) and type(evalf(B[2]), numeric)
		and type(evalf(B[3]), numeric) and type(evalf(B[4]), numeric);
		
		
		Delta[1]:= evalf((B[2]-B[1])/net[1])
		Delta[2]:= evalf((B[4]-B[3])/net[2])
		
		
		Af:= [seq(seq(evalf(r(B[1]+p*Delta[1], B[3]+q*Delta[2])), p=0...net[1]), q=0...net[2])]
		
		questr:= type(sum(sum('evalf(Af[i][k])', 'i'=1...net[1]*net[2]),
		'k'=1...3), 'numeric')
		
		
		if questr and questB and questn :
			
			poly:= (u,v)-> plot3d(r(u+tt,v+ss),
			tt=0...Delta[1], ss=0...Delta[2], grid=[3,3], style=patchnogrid, scaling=constrained):
			
			
			fyld:= display(
			[seq(seq(poly(
			B[1]+p*Delta[1], B[3]+q*Delta[2]),
			p=0...net[1]-1), q=0...net[2]-1)],
			scaling=constrained):
			
			# print(display([base3d(x,y,z), fyld]))
			
			maxi:= k-> max(seq(Af[i][k], i=1...nops(Af)))
			mini:= k-> min(seq(Af[i][k], i=1...nops(Af)))
			extension:= max(seq(maxi(k)-mini(k), k=1...3))
			
			kurveu1:= p-> spacecurve(r(u, B[3]), u=B[1]...(B[1]+p*Delta[1]), color=black, thickness=2):
			
			kurveu2:= p-> spacecurve(r(B[2]+B[1]-u, B[4]), u=B[1]...(B[1]+p*Delta[1]), color=black, thickness=2):
			
			kurvev1:= q-> spacecurve(r(B[1], B[4]+B[3]-v), v=B[3]...(B[3]+q*Delta[2]), color=black, thickness=2):
			
			kurvev2:= q-> spacecurve(r(B[2], v), v=B[3]...(B[3]+q*Delta[2]),  color=black, thickness=2):
			
			for n from 1 to net[1] do
			bd[n]:= display([kurveu1(n)]) od:
			
			for n from net[1]+1 to net[1]+net[2] do
			bd[n]:= display([kurveu1(net[1]), kurvev2(n-net[1])]) od:
			
			for n from net[1]+net[2]+1 to 2*net[1]+net[2] do
			bd[n]:= display([kurveu1(net[1]), kurvev2(net[2]), kurveu2(n-net[1]-net[2])]) od:
			
			for n from 2*net[1]+net[2]+1 to 2*net[1]+2*net[2] do
			bd[n]:= display([kurveu1(net[1]), kurvev2(net[2]), kurveu2(net[1]), kurvev1(n-2*net[1]-net[2])]) od:
			
			randkurv:= display([kurveu1(net[1]), kurvev2(net[2]), kurvev1(net[2]), kurveu2(net[1])])
			
			#anim:= display(seq(bd[p], p=1...2*net[1]+2*net[2]), insequence=true)
			
			
			ku:= (p,q) -> spacecurve(r(u,B[3]+q*Delta[2]), u=B[1]...(B[1]+p*Delta[1]),
			color=red):
			
			kv:= (p,q) -> spacecurve(r(B[1]+p*Delta[1],v), v=B[3]...(B[3]+q*Delta[2]),
			color=blue):
			
			for w from 1 to net[2] do
			for m from 1 to net[1] do
			kou[w,m]:= display([seq(ku(net[1],j), j=0...w-1), seq(ku(i, w), i=1...m)]) od:
			animkou[w]:=  display([randkurv, display(seq(kou[w, p], p=1...net[1]), insequence=true)])
			od:
			
			fullu:= display(seq(ku(net[1],j), j=0...net[2]))
			fullv:= display(seq(kv(j, net[2]), j=0...net[1]))
			
			
			for ww from 1 to net[1] do
			for mm from 1 to net[2] do
			kov[ww,mm]:= display([seq(kv(j, net[2]), j=0...ww-1), seq(kv(ww,i), i=1...mm)]) od:
			animkov[ww]:=  display([fullu, randkurv, display(seq(kov[ww, p], p=1...net[2]), insequence=true)]) od:
			
			
			
			anim:= display(
			seq(bd[p], p=1...2*net[1]+2*net[2]),
			seq(animkou[p], p=1...net[2]),
			seq(animkov[q], q=1...net[1]),
			insequence=true)
			
			display(base3d(x,y,z), anim)
			
		else:
			
	
##################################
########## ORIGINAL ##############
##################################
	
	
	          
	
	##################################################
	
	if nargs=3 then
	net:= netraw;
	if
	type(net[1], numeric) and type(net[2], numeric) then 
	questn:=true else questn:=false;
	net:= [5,5] end if;
	else questn:=false; net:=[5,5] end if;
	
	questB:= type(evalf(B[1]), numeric) and type(evalf(B[2]), numeric)
	and type(evalf(B[3]), numeric) and type(evalf(B[4]), numeric); 
	
	Delta[1]:= evalf((B[2]-B[1])/net[1]);
	Delta[2]:= evalf((B[4]-B[3])/net[2]);
	
	
	Af:= [seq(seq(evalf(r(B[1]+p*Delta[1], B[3]+q*Delta[2])), p=0...net[1]), q=0...net[2])];
	
	questr:= type(sum(sum('evalf(Af[i][k])', 'i'=1...net[1]*net[2]), 
	'k'=1...3), 'numeric');
	
	
	if questr and questB and questn then
	
	poly:= (u,v)-> plot3d(r(u+tt,v+ss), 
	tt=0...Delta[1], ss=0...Delta[2], grid=[3,3], style=patchnogrid, scaling=constrained):
	
	
	fyld:= display(
	[seq(seq(poly(
	B[1]+p*Delta[1], B[3]+q*Delta[2]), 
	p=0...net[1]-1), q=0...net[2]-1)], 
	scaling=constrained):
	
	# print(display([base3d(x,y,z), fyld]));
	
	maxi:= k-> max(seq(Af[i][k], i=1...nops(Af)));
	mini:= k-> min(seq(Af[i][k], i=1...nops(Af)));
	extension:= max(seq(maxi(k)-mini(k), k=1...3));
	
	kurveu1:= p-> spacecurve(r(u, B[3]), u=B[1]...(B[1]+p*Delta[1]), color=black, thickness=2):
	
	kurveu2:= p-> spacecurve(r(B[2]+B[1]-u, B[4]), u=B[1]...(B[1]+p*Delta[1]), color=black, thickness=2):
	
	kurvev1:= q-> spacecurve(r(B[1], B[4]+B[3]-v), v=B[3]...(B[3]+q*Delta[2]), color=black, thickness=2):
	
	kurvev2:= q-> spacecurve(r(B[2], v), v=B[3]...(B[3]+q*Delta[2]),  color=black, thickness=2):
	
	for n from 1 to net[1] do 
	bd[n]:= display([kurveu1(n)]) od:
	
	for n from net[1]+1 to net[1]+net[2] do 
	bd[n]:= display([kurveu1(net[1]), kurvev2(n-net[1])]) od:
	
	for n from net[1]+net[2]+1 to 2*net[1]+net[2] do 
	bd[n]:= display([kurveu1(net[1]), kurvev2(net[2]), kurveu2(n-net[1]-net[2])]) od:
	
	for n from 2*net[1]+net[2]+1 to 2*net[1]+2*net[2] do 
	bd[n]:= display([kurveu1(net[1]), kurvev2(net[2]), kurveu2(net[1]), kurvev1(n-2*net[1]-net[2])]) od:
	
	randkurv:= display([kurveu1(net[1]), kurvev2(net[2]), kurvev1(net[2]), kurveu2(net[1])]);
	
	#anim:= display(seq(bd[p], p=1...2*net[1]+2*net[2]), insequence=true);
	
	
	  ku:= (p,q) -> spacecurve(r(u,B[3]+q*Delta[2]), u=B[1]...(B[1]+p*Delta[1]), 
	            color=red):
	
	  kv:= (p,q) -> spacecurve(r(B[1]+p*Delta[1],v), v=B[3]...(B[3]+q*Delta[2]), 
	            color=blue): 
	
	for w from 1 to net[2] do  
	for m from 1 to net[1] do 
	kou[w,m]:= display([seq(ku(net[1],j), j=0...w-1), seq(ku(i, w), i=1...m)]) od:
	animkou[w]:=  display([randkurv, display(seq(kou[w, p], p=1...net[1]), insequence=true)]) 
	od:
	
	fullu:= display(seq(ku(net[1],j), j=0...net[2]));
	fullv:= display(seq(kv(j, net[2]), j=0...net[1]));
	
	
	for ww from 1 to net[1] do  
	for mm from 1 to net[2] do 
	kov[ww,mm]:= display([seq(kv(j, net[2]), j=0...ww-1), seq(kv(ww,i), i=1...mm)]) od:
	animkov[ww]:=  display([fullu, randkurv, display(seq(kov[ww, p], p=1...net[2]), insequence=true)]) od:
	
	
	
	anim:= display(
	seq(bd[p], p=1...2*net[1]+2*net[2]), 
	seq(animkou[p], p=1...net[2]), 
	seq(animkov[q], q=1...net[1]),
	insequence=true);
	
	display(base3d(x,y,z), anim);
	
	else end if;
	
	
