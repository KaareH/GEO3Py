# GEO3, Python port
# HingeAnalysis
# functions/HingeAnalysis.py


# Description:
# Angles, area, sum of lengths
#
# Globals:  Ar, L, Ang, Llist 
# Locals:   aa, bb, cc, A, dab, dac, dbc, la, lb, lc, Angab, Angac, Angbc  
# Parameters: a::list, b::list
def HingeAnalysis(a, b):
	
	
	###########################################################
	
	 
	###########################################################
	aa:= Vector(a); bb:= Vector(b); cc:= aa-bb; # Kantvektorerne
	la:= Norm(aa); # Længden af kantvektorerne
	lb:= Norm(bb);
	lc:= Norm(cc);
	
	
	if nops(a)=2 then
	A:= Matrix([aa, bb]); # Matrix til bestemmelse af areal, orientering
	Ar:= Determinant(A)/2;
	else
	Ar:= (1/2)*Norm(CrossProduct(aa, bb));
	end if;
	
	
	
	dab:= DotProduct(aa, bb)/(Norm(aa)*Norm(bb)); #Skalarprodukter mellem kantvektorerne
	dac:= DotProduct(aa, cc)/(Norm(aa)*Norm(cc));
	dbc:= DotProduct(-bb, cc)/(Norm(bb)*Norm(cc)); #Note the minus sign!
	
	Angab:= arccos(dab); # Indre vinkler
	Angac:= arccos(dac);
	Angbc:= arccos(dbc);
	
	L:= la+lb+lc; # Omkreds
	
	Llist:= [la, lb, lc]; # Kantlængderne
	
	Ang:= [Angab, Angac, Angbc]: # De indre vinkler på listeform
	
	#############################################################
	# Result: 
	if nops(a)=2 then
	A:= Matrix([aa, bb]); # Matrix til bestemmelse af areal, orientering
	Ar:= Determinant(A)/2;
	else
	Ar:= (1/2)*Norm(CrossProduct(aa, bb));
	end if
	# Result: 
	 nops(a)=2 
	# Result: 
	
	A:= Matrix([aa, bb]); # Matrix til bestemm
	# Result: 
	 af areal, orientering
	Ar:= Determinant(A)/2;
	else
	Ar:= (1/2)*Norm(CrossProduct(aa, bb));
	
	
