# GEO3, Python port
# SVDshow2D
# functions/SVDshow2D.py


# Given column lists of two vectors a and b, the matrix is SVD
decomposed and the corresponding deformation of standard triangle is displayed in 6 moves - the first FLIP only if 
det([a,b]) < 0 and the last parallel translation only if p is given.
# Globals:  rot0, rot1, rot2, defX, defY, parall, tower, stillFin
# Locals:  alpha1, beta1, theta1, alpha2, beta2, theta2, a2, b2, e, f, A, ee, ff,aa,bb,q,
a1, b1, a1m, b1m, figflip, figrot1, figrot2, figscaleX, figscaleY, Id, detA, rot, figparall, figEnd
# Parameters: a::list, b::list, p::list
def SVDshow2D(a::list, b::list, p::list):
	
	
	###########################################################
	
	
	###########################################################
	
	
	if nargs=3 then
	figEnd:= display(Hinge(p, a, b), transparency=0.7)
	else
	figEnd:= display(Hinge([0,0], a, b), transparency=0.7)
	end if;
	
	
	
	
	Id:= IdentityMatrix(2);
	A:= Matrix([a,b]);
	detA:= evalf(Determinant(A));
	
	rot:= t-> Matrix([
	[cos(t), -sin(t)],
	[sin(t), cos(t)]
	]);
	
	
	SVD2D(a,b); 
	
	
	alpha1:= Vt[1,1];
	beta1:= Vt[2,1];
	theta1:= sign(beta1)*arccos(alpha1);
	
	alpha2:= U[1,1];
	beta2:=  U[2,1];
	theta2:= sign(beta2)*arccos(alpha2);
	
	aa:= [(Sigma.Vt.F)[1,1], (Sigma.Vt.F)[2,1]];
	bb:= [(Sigma.Vt.F)[1,2], (Sigma.Vt.F)[2,2]];
	
	if detA >= 0 then 
	ee:= <1,0>; ff:= <0,1>; else
	ee:= <0,1>; ff:= <1,0>; end if;
	
	a2:= aa; b2:= bb;
	
	if detA >= 0 then 
	figrot1:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], convert(rot(t).ee, list), convert(rot(t).ff, list)), title="ROTATION", titlefont=[TIMES,ROMAN, 15]);
	else
	figflip:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], convert(evalm((1-t)*[1,0]  + t*[0,1]), list),  convert(evalm((1-t)*[0,1]  + t*[1,0]), list) ), title="FLIP", titlefont=[TIMES,ROMAN, 15]);
	
	figrot1:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], convert(rot(t).ee, list), convert(rot(t).ff, list)), title="ROTATION", titlefont=[TIMES,ROMAN, 15]);
	end if;
	
	
	figrot2:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], convert(rot(t).Vector(a2), list), convert(rot(t).Vector(b2), list)), title="ROTATION", titlefont=[TIMES,ROMAN, 15]);
	
	
	
	a1:= [(Vt.F)[1,1], (Vt.F)[2,1]]; b1:= [(Vt.F)[1,2], (Vt.F)[2,2]];
	
	
	a1m:= [Sigma[1,1]*(Vt.F)[1,1], (Vt.F)[2,1]]; b1m:= [Sigma[1,1]*(Vt.F)[1,2], (Vt.F)[2,2]];
	
	figscaleX:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], ScaleX(a1,t), ScaleX(b1,t)), title="SKALERING I X-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	figscaleY:= t-> display(Base2d(x,y), figEnd, Hinge([0,0], ScaleY(a1m,t), ScaleY(b1m,t)), title="SKALERING I Y-AKSE-RETNING", titlefont=[TIMES,ROMAN, 15]);
	
	
	
	rot1:= seq(figrot1(theta1*q/40), q=0....40);
	
	defX:= seq(figscaleX((1-(q/40)) + (Sigma[1,1]*q/40)), q=0....40);
	defY:= seq(figscaleY((1-(q/40)) + (Sigma[2,2]*q/40)), q=0....40);
	
	rot2:= seq(figrot2(theta2*q/40), q=0....40);
	
	
	
	if nargs=3 and evalf(Norm(Vector(p))) > 0 then 
	figparall:= t-> display(Base2d(x,y), figEnd, Hinge(t*p, a, b), title="PARALLELFORSKYDNING", titlefont=[TIMES,ROMAN, 15]);
	parall:= seq(figparall(q/20), q=0...20); 
	if detA>=0 then 
	tower:= [rot1, defX, defY, rot2, parall]
	else
	rot0:= seq(figflip(q/20), q=0....20);
	tower:= [rot0, rot1, defX, defY, rot2, parall]
	end if;
	
	else  
	
	if detA>=0 then 
	tower:= [rot1, defX, defY, rot2]
	else
	rot0:= seq(figflip(q/20), q=0....20);
	tower:= [rot0, rot1, defX, defY, rot2]
	end if;
	
	end if;
	
	
	
	
	stillFin:= display(Base2d(x,y), Hinge(p, a,b));
	
	#display(tower, insequence=true);
	
	
	
	
	
	#############################################################
	
