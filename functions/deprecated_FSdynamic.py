# GEO3, Python port
# deprecated_FSdynamic
# functions/deprecated_FSdynamic.py


# Display of Frenet-Serret frame fields t, b, and n 
together with the osculating plane (square of side siz) based on given
parametrization, arc-length or not. Along thin curve. 
Singular points and points of zero curvature 
are tracked down and marked. Single frames are globally accessible: call
FSstill(p), p=1....netraw[1]. 
# Globals: ly accessible: call
FSstill(p), p=1....netraw[1]. "
# Locals:  k, w, i, j, questn, questB, Delta, Af, questr, maxi, mini, 
extension, rP, listSing, listReal, p, q, net, singulStack, rad, pt, 
tang, len, curvat, fragment, FStube, curv, pind1, pind2, pind3, hat1, hat2, hat3, oscPlane,
pil1, pil2, pil3, frame, counter, zeroC, zeroCstack, curveThin, anim, FSanim
# Parameters: r, B, netraw, siz
def deprecated_FSdynamic(r, B, netraw, siz):
	
	
	          
	          global FSstill, FSAll, listCurv, listRealCurv, CurvStack, ex, FSframe;
	
	##################################################
	
	if nargs=4 then
	net:= netraw;
	if
	type(net[1], numeric) then 
	questn:=true else questn:=false;
	net:= [5] end if;
	else questn:=false; net:=[5] end if;
	
	questB:= type(evalf(B[1]), numeric) and type(evalf(B[2]), numeric); 
	
	Delta[1]:= evalf((B[2]-B[1])/net[1]);
	
	Af:= [seq(evalf(r(B[1]+p*Delta[1])), p=0...net[1])];
	
	questr:= type(sum(sum('evalf(Af[i][k])', 'i'=1...net[1]+1), 
	'k'=1...3), numeric);
	
	if questr and questB and questn then
	
	maxi:= k-> max(seq(Af[i,k], i=1...nops(Af)));
	mini:= k-> min(seq(Af[i,k], i=1...nops(Af)));
	extension:= max(seq(maxi(k), k=1...3), seq(-mini(k), k=1..3));
	
	
	
	rP:= unapply(diff(r(u), u), u);
	curv:= unapply(kappaTrunc(r, [u]), u);
	
	
	
	listSing:= [evalf(solve(dot(rP(t), rP(t))=0.0001, t))];
	
	listCurv:= [evalf(solve(evalf(kappa(r, [t]))=1000, t))];
	
	
	
	listReal:= { }:
	if nops(listSing) > 0 then
	for q from 1 to nops(listSing) do
	if type(listSing[q], realcons) then 
	listReal:= listReal union {listSing[q]};
	else end if;
	end do;
	else end if;
	if nops(listReal) > 0 then
	singulStack:= 
	seq(plot3d(evalm(r(listReal[w]) + (extension/25)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
	u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=red), w=1..nops(listReal));
	else singulStack:=NULL; end if;
	
	
	
	
	listRealCurv:= { }:
	if nops(listCurv) > 0 then
	for q from 1 to nops(listCurv) do
	if type(listCurv[q], realcons) then 
	listRealCurv:= listRealCurv union {listCurv[q]};
	else end if;
	end do;
	else end if;
	if nops(listRealCurv) > 0 then
	CurvStack:= 
	seq(plot3d(evalm(r(listRealCurv[w]) + (extension/15)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
	u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=blue), w=1..nops(listRealCurv));
	else CurvStack:=NULL; end if;
	
	
	
	
	rad:= extension/40;
	
	
	#############################################################
	
	 pind1:= u-> tubeplot(evalm(r(u)+t*FStTrunc(r,[u])), 
	                            t=0..0.8, radius=extension/80, grid=[3, 11],
	                            style=patchnogrid, scaling=constrained, 
	                            color=coral):
	  hat1:= u-> tubeplot(evalm(r(u)+t*FStTrunc(r,[u])), 
	     t=0.8...1, radius=(2*(1-t)/0.2)*extension/80,
	                            grid=[3, 7],  style=patch):
	  pil1:= u-> display([pind1(u), hat1(u)]):
	
	
	##############################################################
	  
	 pind2:= u-> tubeplot(evalm(r(u)+t*FSnTrunc(r,[u])), 
	                            t=0..0.8, radius=extension/80, grid=[3, 11],
	                            style=patchnogrid, scaling=constrained, 
	                            color=cyan):
	  hat2:= u-> tubeplot(evalm(r(u)+t*FSnTrunc(r,[u])), 
	     t=0.8...1, radius=(2*(1-t)/0.2)*extension/80,
	                            grid=[3, 7],  style=patch):
	  pil2:= u-> display([pind2(u), hat2(u)]):
	
	
	##################################################
	
	 pind3:= u-> tubeplot(evalm(r(u)+t*FSbTrunc(r,[u])), 
	                            t=0..0.8, radius=extension/80, grid=[3, 11],
	                            style=patchnogrid, scaling=constrained, 
	                            color=sienna):
	  hat3:= u-> tubeplot(evalm(r(u)+t*FSbTrunc(r,[u])), 
	     t=0.8...1, radius=(2*(1-t)/0.2)*extension/80,
	                            grid=[3, 7],  style=patch):
	  pil3:= u-> display([pind3(u), hat3(u)]):
	
	#########################################################
	
	oscPlane:= t-> plot3d(evalm(r(t) + u*FStTrunc(r,[t]) + v*FSnTrunc(r,[t])), 
	u=-siz....siz, v=-siz...siz, color=cyan, grid=[3,3], transparency=0.3):
	
	#########################################################
	
	FSframe:= u-> display(pil1(u), pil2(u), pil3(u), oscPlane(u));
	
	
	counter:= 1;
	
	for p from 1 to net[1] do 
	len:=    min(seq(evalf(nrm(rP(B[1]+(p-(q/10))*Delta[1]))), q=0...10));
	curvat:= min(seq(evalf(curv(  B[1]+(p-(q/10))*Delta[1])), q=0...10));
	if  len > 10^(-3) then 
	if curvat > 10^(-3) then
	frame[p]:= FSframe(evalf(B[1]+((2*p-1)/2)*Delta[1]));
	FSstill[p]:= frame[p]; 
	fragment[p]:=NULL; #MAIN DISCREPANCY: NO FS TUBE HERE
	else
	frame[p]:= NULL;
	fragment[p]:= display(
	spacecurve(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), thickness=2, color=black),
	tubeplot(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), 
	radius=rad, style=wireframe, color=yellow, grid=[3,21]));
	zeroC[counter]:= fragment[p];
	counter:= counter+1;
	end if;
	else frame[p]:= NULL; fragment[p]:=display(
	spacecurve(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), thickness=2, color=black),
	tubeplot(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), 
	radius=rad, style=wireframe, color=yellow, grid=[3,21]));
	end if;
	end do;
	
	
	if counter > 1 then
	zeroCstack:= seq(zeroC[q], q=1...counter-1);
	else zeroCstack:= NULL
	end if;
	
	
	curveThin:= display(seq(fragment[k], k=1...net[1]), spacecurve(r(u), u=B[1]...B[2], thickness=2, color=black));
	
	
	FSAll:= display(base3d(x,y,z), singulStack, zeroCstack, seq(frame[k], k=1...net[1]));
	
	
	anim:= display(seq(frame[k], k=1...net[1]), insequence=true);
	
	ex:= 1.5*max(extension, 2);
	
	FSanim:= display([base3d(x,y,z), singulStack, CurvStack, zeroCstack, curveThin, anim],
	view=[-ex...ex, -ex...ex, -ex...ex]);
	else end if;
	######################
	
