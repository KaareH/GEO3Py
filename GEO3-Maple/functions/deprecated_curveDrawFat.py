# GEO3, Python port
# deprecated_curveDrawFat
# functions/deprecated_curveDrawFat.py


# Description:
# Fat drawing of a given space curve 
# parametrized by r in interval B with netraw. 
# Non-regular points are highlighted. 
# Further output global: static, dynamic: call with display.
#
# Globals: : static, dynamic: call with display."
# Locals:  
k,w, i, j,anim, net, questn, Af,Delta, questr, questB, kurve,  maksval, extension, 
maxi, mini, hs, n, c, res, rP, p, aU, rPOrig, rp, LrP, a, b, rPU, circStak, 
circ, combiner, listSing, listReal, q, t, singulStack, mollif, thinstatic, particle
# Parameters: r, B, netraw
def deprecated_curveDrawFat(r, B, netraw):
	##################################
	########## CONVERTED #############
	##################################
	
	
	
	global static, dynamic
	
	##################################################
	
	if nargs=3 :
		net:= netraw
		if
		type(net[1], numeric) then
		questn:=true else questn:=false
		net:= [5] end if
	else:
		net:=[5] end if
		
		questB:= type(evalf(B[1]), numeric) and type(evalf(B[2]), numeric);
		
		
		Delta[1]:= evalf((B[2]-B[1])/net[1])
		
		Af:= [seq(evalf(r(B[1]+p*Delta[1])), p=0...net[1])]
		
		questr:= type(sum(sum('evalf(Af[i][k])', 'i'=1...net[1]+1),
		'k'=1...3), numeric)
		
		if questr and questB and questn :
			
			maxi:= k-> max(seq(seq(Af[i,k], i=1...nops(Af)), j=1...3))
			mini:= k-> min(seq(seq(Af[i,k], i=1...nops(Af)), j=1...3))
			extension:= max(seq(maxi(k)-mini(k), k=1...3))
			
			kurve:= p-> tubeplot(r(t), t=B[1]...(B[1]+p*Delta[1]),  grid=[5*p+1, 20], radius=extension/70,
			style=patchnogrid, scaling=constrained, projection=0.8, color=cyan):
			
			
			rPOrig:= convert(diff(r(t), t), array)
			
			
			
			for p from 0 to net[1] do
			rp:= evalf(r(B[1]+p*Delta[1]))
			rP:= evalf(subs(t=B[1]+p*Delta[1], eval(rPOrig)))
			LrP:= evalf(dotprod(rP, rP, 'orthogonal'))
			n[0]:= evalf(dotprod(rP, rP, 'orthogonal'))
			c[1]:= evalf(crossprod([1,0,0], rP))
			n[1]:= evalf(dotprod(c[1], c[1], 'orthogonal'))
			c[2]:= evalf(crossprod([0,1,0], rP))
			n[2]:= evalf(dotprod(c[2], c[2], 'orthogonal'))
			c[3]:= evalf(crossprod([0,0,1], rP))
			n[3]:= evalf(dotprod(c[3], c[3], 'orthogonal'))
			
			if LrP > 0 :
				if n[1]>= max(n[2], n[3]) :  res[p]:= 1 else
					if n[2]>= max(n[1], n[3]) :  res[p]:= 2 else
						res[p]:= 3 end if end if
						a[p]:=
						evalm(c[res[p]]/sqrt(dotprod(c[res[p]], c[res[p]], orthogonal)))
						rPU:= rP/sqrt(LrP)
						b[p]:= evalm(crossprod(rPU, a[p]))
						circ[p]:=
						tubeplot(evalm(rp + (extension/60)*cos(v)*a[p] + (extension/60)*sin(v)*b[p]), v=-Pi...Pi, radius=extension/600, color=black)
					else:
						circ[p]:= plot3d(evalm(rp + (extension/48)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
						u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=red) end if
						end do
						
						circStak:= i-> seq(circ[q], q=0...i)
						
						combiner:= i-> display([kurve(i), circStak(i)])
						
						listSing:= [evalf(solve(dotprod(rPOrig, rPOrig, 'orthogonal')=0.001, t))]
						
						listReal:= { }
						
						if nops(listSing) > 0 :
							for q from 1 to nops(listSing) do
							if type(listSing[q], realcons) :
								listReal:= listReal union {listSing[q]}
							else:
								end do
							else:
								
								if nops(listReal) > 0 :
									singulStack:=
									seq(plot3d(evalm(r(listReal[w]) + (extension/30)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
									u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=red), w=1..nops(listReal))
								else:
							
								
								thinstatic:= tubeplot(r(u), u=B[1]...B[2], style=patchnogrid,
								radius=extension/120, grid=[5*net[1], 20], scaling=constrained, projection=0.8, color=cyan):
								
								
								
								
								mollif:= 3
								
								anim:= display([seq(combiner(i), i=1...net[1])], insequence=true)
								
								if nops([singulStack]) > 0 :
									static:= display([combiner(net[1]), singulStack], scaling = constrained, lightmodel = light3, projection = .8);
									
									particle:= i-> display(singulStack, thinstatic, plot3d(
									convert(
									evalm(
									r(B[1]+i*(Delta[1]/mollif)) + (extension/25)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
									list), u=0...Pi, v=-Pi...Pi, grid=[5, 10], style=patchnogrid, color=yellow,
									scaling=constrained, projection=0.8, lightmodel=light4)):
									
									dynamic:= display(seq(particle(k), k=0....mollif*net[1]), insequence=true):
									print(display([anim, base3d(x,y,z), singulStack], scaling=constrained,
									lightmodel=light4, projection=0.8))
								else:
									static:= display(combiner(net[1]), scaling = constrained, lightmodel = light3, projection = .8)
									particle:= i-> display(thinstatic, plot3d(
									convert(
									evalm(
									r(B[1]+i*(Delta[1]/mollif)) + (extension/30)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
									list), u=0...Pi, v=-Pi...Pi, grid=[5, 10], style=patchnogrid, color=yellow,
									scaling=constrained, projection=0.8, lightmodel=light4)):
									dynamic:= display([seq(particle(k), k=0....mollif*net[1])], insequence=true):
									print(display([anim, base3d(x,y,z)], scaling=constrained,
									lightmodel=light4, projection=0.8))
							
								
							else:
								
	
##################################
########## ORIGINAL ##############
##################################
	
	
	          
	          global static, dynamic;
	
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
	
	maxi:= k-> max(seq(seq(Af[i,k], i=1...nops(Af)), j=1...3));
	mini:= k-> min(seq(seq(Af[i,k], i=1...nops(Af)), j=1...3));
	extension:= max(seq(maxi(k)-mini(k), k=1...3));
	
	kurve:= p-> tubeplot(r(t), t=B[1]...(B[1]+p*Delta[1]),  grid=[5*p+1, 20], radius=extension/70,
	style=patchnogrid, scaling=constrained, projection=0.8, color=cyan):
	
	
	rPOrig:= convert(diff(r(t), t), array);
	
	
	
	for p from 0 to net[1] do 
	rp:= evalf(r(B[1]+p*Delta[1]));
	rP:= evalf(subs(t=B[1]+p*Delta[1], eval(rPOrig)));
	LrP:= evalf(dotprod(rP, rP, 'orthogonal'));
	n[0]:= evalf(dotprod(rP, rP, 'orthogonal'));
	c[1]:= evalf(crossprod([1,0,0], rP));
	n[1]:= evalf(dotprod(c[1], c[1], 'orthogonal'));
	c[2]:= evalf(crossprod([0,1,0], rP));
	n[2]:= evalf(dotprod(c[2], c[2], 'orthogonal'));
	c[3]:= evalf(crossprod([0,0,1], rP));
	n[3]:= evalf(dotprod(c[3], c[3], 'orthogonal'));
	
	if LrP > 0 then 
	if n[1]>= max(n[2], n[3]) then  res[p]:= 1 else 
	if n[2]>= max(n[1], n[3]) then  res[p]:= 2 else 
	res[p]:= 3 end if end if;
	a[p]:= 
	evalm(c[res[p]]/sqrt(dotprod(c[res[p]], c[res[p]], orthogonal)));
	rPU:= rP/sqrt(LrP);
	b[p]:= evalm(crossprod(rPU, a[p]));
	circ[p]:= 
	tubeplot(evalm(rp + (extension/60)*cos(v)*a[p] + (extension/60)*sin(v)*b[p]), v=-Pi...Pi, radius=extension/600, color=black)
	else 
	circ[p]:= plot3d(evalm(rp + (extension/48)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
	u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=red) end if
	end do;
	
	circStak:= i-> seq(circ[q], q=0...i);
	
	combiner:= i-> display([kurve(i), circStak(i)]);
	
	listSing:= [evalf(solve(dotprod(rPOrig, rPOrig, 'orthogonal')=0.001, t))];
	
	listReal:= { };
	
	if nops(listSing) > 0 then
	for q from 1 to nops(listSing) do
	if type(listSing[q], realcons) then 
	listReal:= listReal union {listSing[q]};
	else end if;
	end do;
	else end if;
	
	if nops(listReal) > 0 then
	singulStack:= 
	seq(plot3d(evalm(r(listReal[w]) + (extension/30)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]),
	u=0..Pi, v=-Pi..Pi, style=wireframe, grid=[7,14], color=red), w=1..nops(listReal));
	else singulStack:=NULL; end if;
	
	thinstatic:= tubeplot(r(u), u=B[1]...B[2], style=patchnogrid, 
	radius=extension/120, grid=[5*net[1], 20], scaling=constrained, projection=0.8, color=cyan):
	
	
	
	
	mollif:= 3;
	
	anim:= display([seq(combiner(i), i=1...net[1])], insequence=true);
	
	if nops([singulStack]) > 0 then
	static:= display([combiner(net[1]), singulStack], scaling = constrained, lightmodel = light3, projection = .8); 
	particle:= i-> display(singulStack, thinstatic, plot3d(
	convert(
	evalm(
	r(B[1]+i*(Delta[1]/mollif)) + (extension/25)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]), 
	list), u=0...Pi, v=-Pi...Pi, grid=[5, 10], style=patchnogrid, color=yellow,
	scaling=constrained, projection=0.8, lightmodel=light4)):
	
	dynamic:= display(seq(particle(k), k=0....mollif*net[1]), insequence=true):
	print(display([anim, base3d(x,y,z), singulStack], scaling=constrained,
	lightmodel=light4, projection=0.8));
	else 
	static:= display(combiner(net[1]), scaling = constrained, lightmodel = light3, projection = .8);
	particle:= i-> display(thinstatic, plot3d(
	convert(
	evalm(
	r(B[1]+i*(Delta[1]/mollif)) + (extension/30)*[sin(u)*cos(v), sin(u)*sin(v), cos(u)]), 
	list), u=0...Pi, v=-Pi...Pi, grid=[5, 10], style=patchnogrid, color=yellow,
	scaling=constrained, projection=0.8, lightmodel=light4)):
	dynamic:= display([seq(particle(k), k=0....mollif*net[1])], insequence=true):
	print(display([anim, base3d(x,y,z)], scaling=constrained,
	lightmodel=light4, projection=0.8));
	end if;
	
	else end if;
	
	
