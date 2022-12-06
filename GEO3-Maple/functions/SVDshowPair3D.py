# GEO3, Python port
# SVDshowPair3D
# functions/SVDshowPair3D.py


# Description:
# Given column lists of three vectors a, b, and c, the matrix is SVD
# decomposed and the corresponding deformation is displayed in 11 moves --
# the last parallel translation only if p is given.
#
# Globals:  rot0, rot1, rot2, rot3, rot4, rot5, rot6, defX, defY, defZ, tower, stillFin, parall
# Locals:  pp, aa, bb, cc, Uargs, Vtargs, uu, vv, ww, uuu, vvv, www, aaa, bbb, ccc, q, figflip, figscaleX, figscaleY, figscaleZ, a1m, b1m, c1m, a1mm, b1mm, c1mm, fig1, fig2, fig3, fig4, fig5, fig6, A, detA, ee, ff, gg, target, figparall,  rotZ, rotY, rotX, a,b,c,a10,b10,c10,a1t, b1t, c1t, a2t, b2t, c2t, K1, K2, K, p, detK, FF, KK, KK1, KK2
# Parameters: a1::list, b1::list, c1::list, p1::list, a2::list, b2::list, c2::list, p2::list
def SVDshowPair3D(a1, b1, c1, p1, a2, b2, c2, p2):
	##################################
	########## CONVERTED #############
	##################################
	
	
	###########################################################
	
	
	###########################################################
	
	a1t:= Vector(a1);
	b1t:= Vector(b1);
	c1t:= Vector(c1)
	a2t:= Vector(a2);
	b2t:= Vector(b2);
	c2t:= Vector(c2)
	K1:= Matrix([a1t, b1t, c1t]);
	Determinant(K1)
	K2:= Matrix([a2t, b2t, c2t]);
	Determinant(K2)
	
	K:= K2.MatrixInverse(K1)
	
	p:= p2-p1
	
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
	
	
	
	target:= TripodLegs(p2, a2,b2,c2)
	
	FF:= Matrix([ [0,1,0], [1,0,0], [0,0,1] ])
	
	
	detK:= evalf(Determinant(K))
	
	if detK >= 0 :
		KK1:= K1 ;
		KK2:= K2;
	else:
		KK1:= K1.FF;
		KK2:= K2;
	
	
	KK:= KK2.MatrixInverse(KK1)
	
	
	aa:= Column(KK1, 1)
	bb:= Column(KK1, 2)
	cc:= Column(KK1, 3)
	
	
	a:= convert(Column(KK, 1) , list)
	b:= convert(Column(KK, 2) , list)
	c:= convert(Column(KK, 3) , list)
	
	SVD3D(a,b,c);
	
	
	Uargs:= evalf(RotationFactors(U))
	Vtargs:= evalf(RotationFactors(Vt))
	
	
	
	uu:= Vtargs[1];
	vv:=Vtargs[2];
	ww:= Vtargs[3]
	
	figflip:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(evalm((1-t)*[a1[1], a1[2], a1[3]] + t*[aa[1], aa[2], aa[3]]), list), convert( evalm((1-t)*[b1[1], b1[2], b1[3]] + t*[bb[1], bb[2], bb[3]]), list), convert(evalm((1-t)*[c1[1], c1[2], c1[3]] + t*[cc[1], cc[2], cc[3]]) , list)), title="FLIP", titlefont=[TIMES,ROMAN, 15])
	
	fig1:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotX(t*uu).aa , list), convert( rotX(t*uu).bb, list), convert(rotX(t*uu).cc , list)), title="X-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	fig2:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotY(t*vv).rotX(uu).aa , list), convert( rotY(t*vv).rotX(uu).bb, list), convert(rotY(t*vv).rotX(uu).cc , list)), title="Y-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	fig3:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotZ(t*ww).rotY(vv).rotX(uu).aa , list), convert( rotZ(t*ww).rotY(vv).rotX(uu).bb, list), convert(rotZ(t*ww).rotY(vv).rotX(uu).cc , list)), title="Z-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	
	aaa:= Sigma.Vt.aa
	bbb:= Sigma.Vt.bb
	ccc:= Sigma.Vt.cc
	
	
	uuu:= Uargs[1];
	vvv:=Uargs[2];
	www:=Uargs[3]
	
	fig4:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotX(t*uuu).aaa , list), convert( rotX(t*uuu).bbb, list), convert(rotX(t*uuu).ccc , list)), title="X-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	fig5:= t-> display(Base3d(x,y,z), target,  Tripod(p1, convert(rotY(t*vvv).rotX(uuu).aaa , list), convert( rotY(t*vvv).rotX(uuu).bbb, list), convert(rotY(t*vvv).rotX(uuu).ccc , list)), title="Y-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	fig6:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotZ(t*www).rotY(vvv).rotX(uuu).aaa , list), convert( rotZ(t*www).rotY(vvv).rotX(uuu).bbb, list), convert(rotZ(t*www).rotY(vvv).rotX(uuu).ccc , list)), title="Z-ROTATION", titlefont=[TIMES,ROMAN, 15])
	
	
	a10:= convert(Vt.aa , list)
	b10:= convert(Vt.bb, list)
	c10:= convert(Vt.cc , list)
	a1m:= convert(Sigma1.Vt.aa , list)
	b1m:= convert(Sigma1.Vt.bb, list)
	c1m:= convert(Sigma1.Vt.cc , list)
	a1mm:= convert(Sigma2.Sigma1.Vt.aa , list)
	b1mm:= convert(Sigma2.Sigma1.Vt.bb, list)
	c1mm:= convert(Sigma2.Sigma1.Vt.cc , list)
	
	
	
	figscaleX:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleX(a10,t), ScaleX(b10,t), ScaleX(c10,t)), title="SKALERING I X-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	figscaleY:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleY(a1m,t), ScaleY(b1m,t), ScaleY(c1m,t)), title="SKALERING I Y-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	figscaleZ:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleZ(a1mm,t), ScaleZ(b1mm,t), ScaleZ(c1mm,t)), title="SKALERING I Z-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15])
	
	defX:= seq(figscaleX((1-(q/20)) + (Sigma[1,1]*q/20)), q=0....20)
	defY:= seq(figscaleY((1-(q/20)) + (Sigma[2,2]*q/20)), q=0....20)
	defZ:= seq(figscaleZ((1-(q/20)) + (Sigma[3,3]*q/20)), q=0....20)
	
	rot0:=  seq(figflip(q/20), q=0....20)
	
	rot1:= seq(fig1(q/20), q=0....20)
	rot2:= seq(fig2(q/20), q=0....20)
	rot3:= seq(fig3(q/20), q=0....20)
	
	
	rot4:= seq(fig4(q/20), q=0....20)
	rot5:= seq(fig5(q/20), q=0....20)
	rot6:= seq(fig6(q/20), q=0....20)
	
	
	
	
	
	
	if evalf(Norm(Vector(p))) > 0 :
		figparall:= t-> display(Base3d(x,y,z), target, Tripod(p1+t*p, a2, b2, c2), title="PARALLELFORSKYDNING", titlefont=[TIMES,ROMAN, 15])
		parall:= seq(figparall(q/20), q=0...20);
		
		
		if detK>=0 :
			tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall]
		else:
			tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall]
	
		
	else:
		
		if detK>=0 :
			tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6]
		else:
			tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6]
	
		
	
	
	stillFin:= display(Base3d(x,y,z), Tripod(p2, a2,b2,c2))
	
	#display(tower, insequence=true)
	
	
	
	#############################################################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	###########################################################
	
	
	###########################################################
	
	a1t:= Vector(a1); b1t:= Vector(b1); c1t:= Vector(c1);
	a2t:= Vector(a2); b2t:= Vector(b2); c2t:= Vector(c2);
	K1:= Matrix([a1t, b1t, c1t]); Determinant(K1);
	K2:= Matrix([a2t, b2t, c2t]); Determinant(K2);
	
	K:= K2.MatrixInverse(K1);
	
	p:= p2-p1;
	
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
	
	
	target:= TripodLegs(p2, a2,b2,c2);
	
	FF:= Matrix([ [0,1,0], [1,0,0], [0,0,1] ]);
	
	
	detK:= evalf(Determinant(K));
	
	if detK >= 0 then 
	KK1:= K1 ; KK2:= K2; else
	KK1:= K1.FF; KK2:= K2;  end if;
	
	KK:= KK2.MatrixInverse(KK1);
	
	
	aa:= Column(KK1, 1) ;
	bb:= Column(KK1, 2) ;
	cc:= Column(KK1, 3) ;
	
	
	a:= convert(Column(KK, 1) , list);
	b:= convert(Column(KK, 2) , list);
	c:= convert(Column(KK, 3) , list);
	
	SVD3D(a,b,c); 
	
	Uargs:= evalf(RotationFactors(U));
	Vtargs:= evalf(RotationFactors(Vt));
	
	
	
	uu:= Vtargs[1]; vv:=Vtargs[2]; ww:= Vtargs[3];
	
	figflip:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(evalm((1-t)*[a1[1], a1[2], a1[3]] + t*[aa[1], aa[2], aa[3]]), list), convert( evalm((1-t)*[b1[1], b1[2], b1[3]] + t*[bb[1], bb[2], bb[3]]), list), convert(evalm((1-t)*[c1[1], c1[2], c1[3]] + t*[cc[1], cc[2], cc[3]]) , list)), title="FLIP", titlefont=[TIMES,ROMAN, 15]);
	
	fig1:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotX(t*uu).aa , list), convert( rotX(t*uu).bb, list), convert(rotX(t*uu).cc , list)), title="X-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	fig2:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotY(t*vv).rotX(uu).aa , list), convert( rotY(t*vv).rotX(uu).bb, list), convert(rotY(t*vv).rotX(uu).cc , list)), title="Y-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	fig3:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotZ(t*ww).rotY(vv).rotX(uu).aa , list), convert( rotZ(t*ww).rotY(vv).rotX(uu).bb, list), convert(rotZ(t*ww).rotY(vv).rotX(uu).cc , list)), title="Z-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	
	aaa:= Sigma.Vt.aa;
	bbb:= Sigma.Vt.bb;
	ccc:= Sigma.Vt.cc;
	
	
	uuu:= Uargs[1]; vvv:=Uargs[2]; www:=Uargs[3];
	
	fig4:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotX(t*uuu).aaa , list), convert( rotX(t*uuu).bbb, list), convert(rotX(t*uuu).ccc , list)), title="X-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	fig5:= t-> display(Base3d(x,y,z), target,  Tripod(p1, convert(rotY(t*vvv).rotX(uuu).aaa , list), convert( rotY(t*vvv).rotX(uuu).bbb, list), convert(rotY(t*vvv).rotX(uuu).ccc , list)), title="Y-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	fig6:= t-> display(Base3d(x,y,z), target, Tripod(p1, convert(rotZ(t*www).rotY(vvv).rotX(uuu).aaa , list), convert( rotZ(t*www).rotY(vvv).rotX(uuu).bbb, list), convert(rotZ(t*www).rotY(vvv).rotX(uuu).ccc , list)), title="Z-ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	
	a10:= convert(Vt.aa , list);
	b10:= convert(Vt.bb, list);
	c10:= convert(Vt.cc , list);
	a1m:= convert(Sigma1.Vt.aa , list);
	b1m:= convert(Sigma1.Vt.bb, list);
	c1m:= convert(Sigma1.Vt.cc , list);
	a1mm:= convert(Sigma2.Sigma1.Vt.aa , list);
	b1mm:= convert(Sigma2.Sigma1.Vt.bb, list);
	c1mm:= convert(Sigma2.Sigma1.Vt.cc , list);
	
	
	
	figscaleX:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleX(a10,t), ScaleX(b10,t), ScaleX(c10,t)), title="SKALERING I X-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	figscaleY:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleY(a1m,t), ScaleY(b1m,t), ScaleY(c1m,t)), title="SKALERING I Y-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	figscaleZ:= t-> display(Base3d(x,y,z), target, Tripod(p1, ScaleZ(a1mm,t), ScaleZ(b1mm,t), ScaleZ(c1mm,t)), title="SKALERING I Z-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	defX:= seq(figscaleX((1-(q/20)) + (Sigma[1,1]*q/20)), q=0....20);
	defY:= seq(figscaleY((1-(q/20)) + (Sigma[2,2]*q/20)), q=0....20);
	defZ:= seq(figscaleZ((1-(q/20)) + (Sigma[3,3]*q/20)), q=0....20);
	
	rot0:=  seq(figflip(q/20), q=0....20);
	
	rot1:= seq(fig1(q/20), q=0....20);
	rot2:= seq(fig2(q/20), q=0....20);
	rot3:= seq(fig3(q/20), q=0....20);
	
	
	rot4:= seq(fig4(q/20), q=0....20);
	rot5:= seq(fig5(q/20), q=0....20);
	rot6:= seq(fig6(q/20), q=0....20);
	
	
	
	
	
	
	if evalf(Norm(Vector(p))) > 0 then 
	figparall:= t-> display(Base3d(x,y,z), target, Tripod(p1+t*p, a2, b2, c2), title="PARALLELFORSKYDNING", titlefont=[TIMES,ROMAN, 15]);
	parall:= seq(figparall(q/20), q=0...20); 
	
	if detK>=0 then 
	tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall];
	else 
	tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6, parall];
	end if;
	
	else
	
	if detK>=0 then 
	tower:= [rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6];
	else 
	tower:= [rot0, rot1, rot2, rot3, defX, defY, defZ, rot4, rot5, rot6];
	end if;
	
	 end if;
	
	stillFin:= display(Base3d(x,y,z), Tripod(p2, a2,b2,c2));
	
	#display(tower, insequence=true);
	
	
	
	#############################################################
	
