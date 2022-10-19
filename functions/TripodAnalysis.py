# GEO3, Python port
# TripodAnalysis
# functions/TripodAnalysis.py


# Lengths of edges, areas of faces, volume
# Globals:  Vol, Llist, Alist, Area, L 
# Locals:   aa, bb, cc, ba, ca, cb, laa, lbb, lcc, lba, lca,lcb, V, 
Aab, Aac, Abc, Abaca,   A, dab, dac, dbc, la, lb, lc
# Parameters: a::list, b::list, c::list
def TripodAnalysis(a::list, b::list, c::list):
	
	
	###########################################################
	
	###########################################################
	 
	###########################################################
	
	aa:= Vector(a); 
	bb:= Vector(b); 
	cc:= Vector(c);
	
	
	ba:=  Vector(b-a); 
	ca:=  Vector(c-a); 
	cb:=  Vector(c-b); 
	
	
	# Længden af kantvektorerne
	
	laa:= Norm(aa); 
	lbb:= Norm(bb);
	lcc:= Norm(cc);
	lba:= Norm(ba);
	lca:= Norm(ca);
	lcb:= Norm(cb);
	
	L:= laa+lbb+lcc+lba+lca+lcb; # Totale kantlængde
	
	Llist:= [laa, lbb, lcc, lba, lca, lcb]; # Kantlængderne på listeform
	
	V:= Matrix([aa, bb, cc]); # Matrix til bestemmelse af rumfang, orientering
	
	Vol:= Determinant(V)/6;
	
	Aab:=   Norm(CrossProduct(aa, bb))/2;
	Aac:=   Norm(CrossProduct(aa, cc))/2;
	Abc:=   Norm(CrossProduct(bb, cc))/2;
	Abaca:= Norm(CrossProduct(ba, ca))/2;
	
	Alist:= [Aab, Aac, Abc, Abaca];
	
	Area:= Aab+Aac+Abc+Abaca;
	
	
	#############################################################
	
