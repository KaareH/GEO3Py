# GEO3, Python port
# deprecated_FSstatic
# functions/deprecated_FSstatic.py


# Description:
# Display of Frenet-Serret oriented fat tube in given
# parametrization, arc-length or not. The tube has square cross section.
# The normals to the tube-faces are the n and b fields resp.
# Singular points (red) and points close to zero curvature (yellowish)
# are marked in order to prepare for breakdown of Frenet-Serret apparatus.
#
# Globals: 
# Locals:  k, w, i, j, questn, questB, Delta, Af, questr, maxi, mini, 
extension, rP, listSing, listReal, p, q, net, singulStack, rad, pt, 
tang, len, curvat, fragment, FStube, curv, listCurv, listRealCurv, CurvStack, counter, zeroC,
zeroCstack, ex
# Parameters: r, B, netraw
def deprecated_FSstatic(r, B, netraw):
	
	
	          
	
	##################################################
	
	if nargs=3 then
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
	
	counter:= 1;
	
	for p from 1 to net[1] do 
	len:=    min(seq(evalf(nrm(rP(B[1]+(p-(q/10))*Delta[1]))), q=0...10));
	curvat:= min(seq(evalf(curv(  B[1]+(p-(q/10))*Delta[1])), q=0...10));
	if  len > 10^(-3) then 
	if curvat > 10^(-3) then 
	fragment[p]:= 
	plot3d(evalm(r(u) + (rad)*cos(v+(Pi/4))*(FSbTrunc(r, [u])) + 
	(rad)*sin(v+(Pi/4))*(FSnTrunc(r, [u]))), 
	u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), v=-Pi...Pi, grid=[3, 5], scaling=constrained);
	else
	
	fragment[p]:= display(spacecurve(r(u), 
	u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), thickness=2, color=black),
	tubeplot(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), 
	radius=rad, style=wireframe, color=yellow, grid=[3,21]));
	zeroC[counter]:= fragment[p];
	end if;
	else fragment[p]:=display(spacecurve(r(u), 
	u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), thickness=2, color=black),
	tubeplot(r(u), u=evalf(B[1]+(p-1)*Delta[1])...evalf(B[1]+p*Delta[1]), 
	radius=rad, style=wireframe, color=yellow, grid=[3,21]));
	end if;
	end do;
	
	
	if counter > 1 then
	zeroCstack:= seq(zeroC[q], q=1...counter-1);
	else zeroCstack:= NULL
	end if;
	
	ex:= 1.5*max(extension, 2);
	
	display([base3d(x,y,z), singulStack, CurvStack, zeroCstack, seq(fragment[k], k=1....net[1])], 
	view=[-ex...ex, -ex...ex, -ex...ex]):
	
	else end if;
	# Result: 
	if nargs=3 then
	net:= netraw;
	if
	type(net[1], numeric) then 
	questn:=true else questn:=false;
	net:= [5] end if
	# Result: 
	 nargs=3 
	# Result: 
	
	net:= netraw;
	if
	type(net[1], numeric) then 
	questn:=true 
	# Result: 
	 questn:=false;
	net:= [5] 
	
