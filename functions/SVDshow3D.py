# GEO3, Python port
# SVDshow3D
# functions/SVDshow3D.py


# Description:
# Given column lists of three vectors a, b, and c, the matrix is SVD
# decomposed and the corresponding deformation of standard tripod is displayed in 6 or 7 moves, the first flip only if det(a,b,c)<0, 
# the last parallel translation only if p is given.
#
# Globals:  rot0, rot1, rot2, rot3, rot4, rot5, rot6, defX, defY, defZ, tower, stillFin
# Locals:  pp, aa, bb, cc, Uargs, Vtargs, uu, vv, ww, uuu, vvv, www, aaa, bbb, ccc, q, figflip, figscaleX, figscaleY, figscaleZ, a1, b1, c1, a1m, b1m, c1m, a1mm, b1mm, c1mm, fig1, fig2, fig3, fig4, fig5, fig6, A, detA, ee, ff, gg, target, figparall, parall, rotZ, rotY, rotX
# Parameters: a::list, b::list, c::list, p::list
def SVDshow3D(a, b, c, p):
	##################################
	########## CONVERTED #############
	##################################
	
	
	###########################################################
	
	
	###########################################################
	
	
	
	
	rotZ:= t-> Matrix([
	[cos(t), -sin(t),0],
	[sin(t), cos(t), 0],
	[0,0,1]
	]);
	
	
	rotY:= t-> Matrix([
	[cos(t), 0, -sin(t)],
	[0, 1, 0],
	[sin(t),0,cos(t)]
	]);
	
	
	rotX:= t-> Matrix([
	[1, 0,0],
	[0, cos(t), -sin(t)],
	[0, sin(t), cos(t)]
	]);
	
	
	
	
	
	
	
	target:= TripodLegs(p, a,b,c)
	
	A:= Matrix([a,b,c])
	detA:= evalf(Determinant(A))
	
	if detA >= 0 :
		ee:= <1,0,0>;
		ff:= <0,1,0>;
		gg:=<0,0,1>;
	else:
		ee:= <0,1,0>;
		ff:= <1,0,0>;
		gg:=<0,0,1>;
	
	
	
	#aa:= Vector(a)
	#bb:= Vector(b)
	#cc:= Vector(c)
	
	aa:= ee;
	bb:= ff;
	cc:= gg
	
	
	SVD3D(a,b,c);
	
	
	Uargs:= evalf(RotationFactors(U))
	Vtargs:= evalf(RotationFactors(Vt))
	
	
	
	uu:= Vtargs[1];
	vv:=Vtargs[2];
	ww:= Vtargs[3]
	
	
	
	figflip:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(evalm((1-t)*[1,0,0] + t*[0,1,0]), list), convert(evalm((1-t)*[0,1,0] + t*[1,0,0]), list), [0,0,1]), title="FLIP", titlefont=[TIMES,ROMAN, 15])
	
	fig1:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotX(t*uu).aa , list), convert( rotX(t*uu).bb, list), convert(rotX(t*uu).cc , list)), title="ROTATION OM X-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	fig2:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotY(t*vv).rotX(uu).aa , list), convert( rotY(t*vv).rotX(uu).bb, list), convert(rotY(t*vv).rotX(uu).cc , list)), title="ROTATION OM Y-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	fig3:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotZ(t*ww).rotY(vv).rotX(uu).aa , list), convert( rotZ(t*ww).rotY(vv).rotX(uu).bb, list), convert(rotZ(t*ww).rotY(vv).rotX(uu).cc , list)), title="ROTATION OM Z-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	
	aaa:= Sigma.Vt.aa
	bbb:= Sigma.Vt.bb
	ccc:= Sigma.Vt.cc
	
	
	uuu:= Uargs[1];
	vvv:=Uargs[2];
	www:=Uargs[3]
	
	fig4:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotX(t*uuu).aaa , list), convert( rotX(t*uuu).bbb, list), convert(rotX(t*uuu).ccc , list)), title="ROTATION OM X-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	fig5:= t-> display(Base3d(x,y,z), target,  Tripod([0,0,0], convert(rotY(t*vvv).rotX(uuu).aaa , list), convert( rotY(t*vvv).rotX(uuu).bbb, list), convert(rotY(t*vvv).rotX(uuu).ccc , list)), title="ROTATION OM Y-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	fig6:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotZ(t*www).rotY(vvv).rotX(uuu).aaa , list), convert( rotZ(t*www).rotY(vvv).rotX(uuu).bbb, list), convert(rotZ(t*www).rotY(vvv).rotX(uuu).ccc , list)), title="ROTATION OM Z-AKSEN", titlefont=[TIMES,ROMAN, 15])
	
	
	a1:= convert(Vt.aa , list)
	b1:= convert(Vt.bb, list)
	c1:= convert(Vt.cc , list)
	a1m:= convert(Sigma1.Vt.aa , list)
	b1m:= convert(Sigma1.Vt.bb, list)
	c1m:= convert(Sigma1.Vt.cc , list)
	a1mm:= convert(Sigma2.Sigma1.Vt.aa , list)
	b1mm:= convert(Sigma2.Sigma1.Vt.bb, list)
	c1mm:= convert(Sigma2.Sigma1.Vt.cc , list)
	
	
	
	figscaleX:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleX(a1,t), ScaleX(b1,t), ScaleX(c1,t)), title="SKALERING I X-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	figscaleY:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleY(a1m,t), ScaleY(b1m,t), ScaleY(c1m,t)), title="SKALERING I Y-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	figscaleZ:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleZ(a1mm,t), ScaleZ(b1mm,t), ScaleZ(c1mm,t)), title="SKALERING I Z-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	defX:= seq(figscaleX((1-(q/20)) + (Sigma[1,1]*q/20)), q=0....20)
	defY:= seq(figscaleY((1-(q/20)) + (Sigma[2,2]*q/20)), q=0....20)
	defZ:= seq(figscaleZ((1-(q/20)) + (Sigma[3,3]*q/20)), q=0....20)
	
	
	rot0:= seq(figflip(q/20), q=0....20)
	
	rot1:= seq(fig1(q/20), q=0....20)
	rot2:= seq(fig2(q/20), q=0....20)
	rot3:= seq(fig3(q/20), q=0....20)
	
	
	rot4:= seq(fig4(q/20), q=0....20)
	rot5:= seq(fig5(q/20), q=0....20)
	rot6:= seq(fig6(q/20), q=0....20)
	
	
	
	
	
	
	if nargs=4 and evalf(Norm(Vector(p))) > 0 :
		figparall:= t-> display(Base3d(x,y,z), target, Tripod(t*p, a, b, c), title="PARALLELFORSKYDNING", titlefont=[TIMES,ROMAN, 15])
		parall:= seq(figparall(q/20), q=0...20);
		
		if detA>=0 :
			tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall]
		else:
			tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall]
	
		
	else:
		if detA>=0 :
			tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6]
		else:
			tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6]
	
		
		
	
	
	stillFin:= display(Base3d(x,y,z), Tripod(p, a,b,c))
	
	#display(tower, insequence=true)
	
	
	
	#############################################################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	###########################################################
	
	
	###########################################################
	
	
	
	
	rotZ:= t-> Matrix([
	[cos(t), -sin(t),0], 
	[sin(t), cos(t), 0],
	[0,0,1]
	]); 
	
	rotY:= t-> Matrix([
	[cos(t), 0, -sin(t)], 
	[0, 1, 0],
	[sin(t),0,cos(t)]
	]); 
	
	rotX:= t-> Matrix([
	[1, 0,0],
	[0, cos(t), -sin(t)], 
	[0, sin(t), cos(t)]
	]); 
	
	
	
	
	
	
	target:= TripodLegs(p, a,b,c);
	
	A:= Matrix([a,b,c]);
	detA:= evalf(Determinant(A));
	
	if detA >= 0 then 
	ee:= <1,0,0>; ff:= <0,1,0>; gg:=<0,0,1>; else
	ee:= <0,1,0>; ff:= <1,0,0>; gg:=<0,0,1>; end if;
	
	
	#aa:= Vector(a);
	#bb:= Vector(b);
	#cc:= Vector(c);
	
	aa:= ee; bb:= ff; cc:= gg;
	
	
	SVD3D(a,b,c); 
	
	Uargs:= evalf(RotationFactors(U));
	Vtargs:= evalf(RotationFactors(Vt));
	
	
	
	uu:= Vtargs[1]; vv:=Vtargs[2]; ww:= Vtargs[3];
	
	
	
	figflip:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(evalm((1-t)*[1,0,0] + t*[0,1,0]), list), convert(evalm((1-t)*[0,1,0] + t*[1,0,0]), list), [0,0,1]), title="FLIP", titlefont=[TIMES,ROMAN, 15]);
	
	fig1:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotX(t*uu).aa , list), convert( rotX(t*uu).bb, list), convert(rotX(t*uu).cc , list)), title="ROTATION OM X-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	fig2:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotY(t*vv).rotX(uu).aa , list), convert( rotY(t*vv).rotX(uu).bb, list), convert(rotY(t*vv).rotX(uu).cc , list)), title="ROTATION OM Y-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	fig3:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotZ(t*ww).rotY(vv).rotX(uu).aa , list), convert( rotZ(t*ww).rotY(vv).rotX(uu).bb, list), convert(rotZ(t*ww).rotY(vv).rotX(uu).cc , list)), title="ROTATION OM Z-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	
	aaa:= Sigma.Vt.aa;
	bbb:= Sigma.Vt.bb;
	ccc:= Sigma.Vt.cc;
	
	
	uuu:= Uargs[1]; vvv:=Uargs[2]; www:=Uargs[3];
	
	fig4:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotX(t*uuu).aaa , list), convert( rotX(t*uuu).bbb, list), convert(rotX(t*uuu).ccc , list)), title="ROTATION OM X-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	fig5:= t-> display(Base3d(x,y,z), target,  Tripod([0,0,0], convert(rotY(t*vvv).rotX(uuu).aaa , list), convert( rotY(t*vvv).rotX(uuu).bbb, list), convert(rotY(t*vvv).rotX(uuu).ccc , list)), title="ROTATION OM Y-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	fig6:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], convert(rotZ(t*www).rotY(vvv).rotX(uuu).aaa , list), convert( rotZ(t*www).rotY(vvv).rotX(uuu).bbb, list), convert(rotZ(t*www).rotY(vvv).rotX(uuu).ccc , list)), title="ROTATION OM Z-AKSEN", titlefont=[TIMES,ROMAN, 15]);
	
	
	a1:= convert(Vt.aa , list);
	b1:= convert(Vt.bb, list);
	c1:= convert(Vt.cc , list);
	a1m:= convert(Sigma1.Vt.aa , list);
	b1m:= convert(Sigma1.Vt.bb, list);
	c1m:= convert(Sigma1.Vt.cc , list);
	a1mm:= convert(Sigma2.Sigma1.Vt.aa , list);
	b1mm:= convert(Sigma2.Sigma1.Vt.bb, list);
	c1mm:= convert(Sigma2.Sigma1.Vt.cc , list);
	
	
	
	figscaleX:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleX(a1,t), ScaleX(b1,t), ScaleX(c1,t)), title="SKALERING I X-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	figscaleY:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleY(a1m,t), ScaleY(b1m,t), ScaleY(c1m,t)), title="SKALERING I Y-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	figscaleZ:= t-> display(Base3d(x,y,z), target, Tripod([0,0,0], ScaleZ(a1mm,t), ScaleZ(b1mm,t), ScaleZ(c1mm,t)), title="SKALERING I Z-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	defX:= seq(figscaleX((1-(q/20)) + (Sigma[1,1]*q/20)), q=0....20);
	defY:= seq(figscaleY((1-(q/20)) + (Sigma[2,2]*q/20)), q=0....20);
	defZ:= seq(figscaleZ((1-(q/20)) + (Sigma[3,3]*q/20)), q=0....20);
	
	
	rot0:= seq(figflip(q/20), q=0....20);
	
	rot1:= seq(fig1(q/20), q=0....20);
	rot2:= seq(fig2(q/20), q=0....20);
	rot3:= seq(fig3(q/20), q=0....20);
	
	
	rot4:= seq(fig4(q/20), q=0....20);
	rot5:= seq(fig5(q/20), q=0....20);
	rot6:= seq(fig6(q/20), q=0....20);
	
	
	
	
	
	
	if nargs=4 and evalf(Norm(Vector(p))) > 0 then 
	figparall:= t-> display(Base3d(x,y,z), target, Tripod(t*p, a, b, c), title="PARALLELFORSKYDNING", titlefont=[TIMES,ROMAN, 15]);
	parall:= seq(figparall(q/20), q=0...20); 
	if detA>=0 then 
	tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall]
	else
	tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall];
	end if;
	
	else
	if detA>=0 then 
	tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6]
	else
	tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6];
	end if;
	
	
	end if;
	
	stillFin:= display(Base3d(x,y,z), Tripod(p, a,b,c));
	
	#display(tower, insequence=true);
	
	
	
	#############################################################
	
