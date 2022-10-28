# GEO3, Python port
# SVD3D
# functions/SVD3D.py


# Description:
# SVD baseret 4-faktor split af given matrix med søjle-vektorer a og b og c.
# Out: Original SVD 
#
# Globals:  Sigma, Sigma1, Sigma2, Sigma3, U, Vt, F, Energy
# Locals:  SingValDec, Uraw, Vtraw, detAA, A, AA
# Parameters: a::list, b::list, c::list
def SVD3D(a, b, c):
	
	
	####################
	
	####################
	
	####################
	      
	
	AA:= evalf(Matrix([
	[a[1], b[1], c[1]],
	[a[2], b[2], c[2]],
	[a[3], b[3], c[3]]
	]));
	
	
	
	detAA:= Determinant(AA);
	
	if detAA < 0 then 
	F:= Matrix([
	[0, 1., 0], 
	[1., 0, 0],
	[0, 0, 1.]
	]);
	A:= evalf(AA.F); else
	A:= evalf(AA); 
	F:= IdentityMatrix(3);
	end if;
	
	
	
	SingValDec:= [SingularValues(A, output=['U', 'S', 'Vt'])];
	
	Uraw:= SingValDec[1];
	
	Sigma:= DiagonalMatrix(SingValDec[2]);
	
	Sigma1:= DiagonalMatrix([Sigma[1,1], 1, 1]);
	Sigma2:= DiagonalMatrix([1, Sigma[2,2], 1]);
	Sigma3:= DiagonalMatrix([1, 1, Sigma[3,3]]);
	
	Energy:= (1-Sigma[1,1])^2 + (1-Sigma[2,2])^2 + (1-Sigma[3,3])^2;
	
	Vtraw:= SingValDec[3];
	
	# Guarantee that the 'first' rotation is chosen positively 
	# oriented obtain by changing sign on first Vt row and then
	# corresondingly change sign on first U column:
	
	if Determinant(Vtraw) < 0 then 
	Vt:= RowOperation(Vtraw, 1, -1);
	else
	Vt:= Vtraw;
	end if;
	
	
	if Determinant(Vtraw) < 0 then 
	U:= ColumnOperation(Uraw, 1, -1);
	else
	U:= Uraw;
	end if;
	
	
	####################
	# Result: 
	if detAA < 0 then 
	F:= Matrix([
	[0, 1., 0], 
	[1., 0, 0],
	[0, 0, 1.]
	]);
	A:= evalf(AA.F); else
	A:= evalf(AA); 
	F:= IdentityMatrix(3);
	end if
	# Result: 
	 detAA < 0 
	# Result: 
	 
	F:= Matrix([
	[0, 1., 0], 
	[1., 0, 0],
	[0, 0, 1.]
	]);
	A:= evalf(AA.F); 
	# Result: 
	
	A:= evalf(AA); 
	F:= IdentityMatrix(3);
	
	
