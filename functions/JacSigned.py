# GEO3, Python port
# JacSigned
# functions/JacSigned.py


# Description:
# Jacobi-function of vector function r 
# : L=[u]; L=[u,v]; eller L=[u,v,w].
# Target space R^3.
#
# Globals: 
# Locals:  Jacobi, rP, uTang, vTang, wTang, A, Kryds  
# Parameters: r, L
def JacSigned(r, L):
	
	
	          
	          
	############################################
	
	if nops(L)=1 then
	
	rP:= unapply(convert(diff(r(u), u), D), u);
	Jacobi:= u-> simplify(sqrt(dotprod(rP(u), rP(u), 'orthogonal')));
	Jacobi(L[1]);
	############################################
	
	else
	if nops(L)=2 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v), u), D)), u,v);
	vTang:= unapply(simplify(convert(diff(r(u,v), v), D)), u,v);
	Kryds:= (u,v)-> crossprod(uTang(u,v), vTang(u,v));
	Jacobi:= (u,v)-> simplify(sqrt(combine(dotprod(Kryds(u,v), Kryds(u,v), 'orthogonal'))));
	Jacobi(L[1], L[2]);
	############################################
	
	else
	if nops(L)=3 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v,w), u), D)), u,v,w);
	vTang:= unapply(simplify(convert(diff(r(u,v,w), v), D)), u,v,w);
	wTang:= unapply(simplify(convert(diff(r(u,v,w), w), D)), u,v,w);
	A:= (u,v,w)-> augment(uTang(u,v,w), vTang(u,v,w), wTang(u,v,w)):
	Jacobi:= (u,v,w)-> simplify(det(A(u,v,w))):
	Jacobi(L[1], L[2], L[3]);
	##################################################
	
	end if
	end if
	end if
	
	##################################################
	# Result: 
	if nops(L)=1 then
	
	rP:= unapply(convert(diff(r(u), u), D), u);
	Jacobi:= u-> simplify(sqrt(dotprod(rP(u), rP(u), 'orthogonal')));
	Jacobi(L[1]);
	############################################
	
	else
	if nops(L)=2 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v), u), D)), u,v);
	vTang:= unapply(simplify(convert(diff(r(u,v), v), D)), u,v);
	Kryds:= (u,v)-> crossprod(uTang(u,v), vTang(u,v));
	Jacobi:= (u,v)-> simplify(sqrt(combine(dotprod(Kryds(u,v), Kryds(u,v), 'orthogonal'))));
	Jacobi(L[1], L[2]);
	############################################
	
	else
	if nops(L)=3 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v,w), u), D)), u,v,w);
	vTang:= unapply(simplify(convert(diff(r(u,v,w), v), D)), u,v,w);
	wTang:= unapply(simplify(convert(diff(r(u,v,w), w), D)), u,v,w);
	A:= (u,v,w)-> augment(uTang(u,v,w), vTang(u,v,w), wTang(u,v,w)):
	Jacobi:= (u,v,w)-> simplify(det(A(u,v,w))):
	Jacobi(L[1], L[2], L[3]);
	##################################################
	
	end if
	# Result: 
	 nops(L)=1 
	# Result: 
	
	
	rP:= unapply(convert(diff(r(u), u), D), u);
	Jacobi:= u-> simplify(sqrt(dotprod(rP(u), rP(u), 'orthogonal')));
	Jacobi(L[1]);
	############################################
	
	
	# Result: 
	
	if nops(L)=2 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v), u), D)), u,v);
	vTang:= unapply(simplify(convert(diff(r(u,v), v), D)), u,v);
	Kryds:= (u,v)-> crossprod(uTang(u,v), vTang(u,v));
	Jacobi:= (u,v)-> simplify(sqrt(combine(dotprod(Kryds(u,v), Kryds(u,v), 'orthogonal'))));
	Jacobi(L[1], L[2]);
	############################################
	
	else
	if nops(L)=3 then
	
	uTang:= unapply(simplify(convert(diff(r(u,v,w), u), D)), u,v,w);
	vTang:= unapply(simplify(convert(diff(r(u,v,w), v), D)), u,v,w);
	wTang:= unapply(simplify(convert(diff(r(u,v,w), w), D)), u,v,w);
	A:= (u,v,w)-> augment(uTang(u,v,w), vTang(u,v,w), wTang(u,v,w)):
	Jacobi:= (u,v,w)-> simplify(det(A(u,v,w))):
	Jacobi(L[1], L[2], L[3]);
	##################################################
	
	
	
