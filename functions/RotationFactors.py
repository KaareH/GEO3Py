# GEO3, Python port
# RotationFactors
# functions/RotationFactors.py


# Given orthogonal 3x3 matrix R decompose it into R = rotZ(w).rotY(v).rotX(u) and output: arguments [u,v,w] in  list.
# Globals: 
# Locals:  rot, uu, vv, ww, G, i
# Parameters: R::Matrix
def RotationFactors(R::Matrix):
	
	
	###########################################################
	
	###########################################################
	
	
	rot:= (u,v,w)-> Matrix(3, 3, {(1, 1) = cos(w)*cos(v), (1, 2) = -sin(w)*cos(u)-cos(w)*sin(v)*sin(u), (1, 3) = sin(w)*sin(u)-cos(w)*sin(v)*cos(u), (2, 1) = sin(w)*cos(v), (2, 2) = cos(w)*cos(u)-sin(w)*sin(v)*sin(u), (2, 3) = -cos(w)*sin(u)-sin(w)*sin(v)*cos(u), (3, 1) = sin(v), (3, 2) = cos(v)*sin(u), (3, 3) = cos(v)*cos(u)});
	
	# Values in [-Pi/2, Pi/2]: 
	
	vv:= arcsin(R[3,1]);
	
	if evalf(abs(vv - Pi/2))<10^(-6) then uu:= 0; ww:= arccos(R[2,2]); else end if;
	if evalf(abs(vv + Pi/2))<10^(-6) then uu:= 0; ww:= -arccos(R[2,2]); else end if;
	
	if evalf(abs(cos(vv)))>10^(-6) then  uu:= arcsin(R[3,2]/cos(vv)); ww:= arccos(R[1,1]/cos(vv)); else end if;
	
	
	
	# Check for correct modification in [-Pi, Pi] :
	
	G[1]:= [MatrixNorm(evalf((rot(uu,vv,ww))-R)),          [uu,vv,ww]];
	G[2]:= [MatrixNorm(evalf((rot(Pi-uu,vv,ww))-R)),       [Pi-uu,vv,ww]];
	G[3]:= [MatrixNorm(evalf((rot(uu,Pi-vv,ww))-R)),       [uu, Pi-vv,ww]];
	G[4]:= [MatrixNorm(evalf((rot(uu,vv,-ww))-R)),         [uu,vv,-ww]];;
	G[5]:= [MatrixNorm(evalf((rot(Pi-uu,Pi-vv,ww))-R)),    [Pi-uu,Pi-vv,ww]];
	G[6]:= [MatrixNorm(evalf((rot(uu,Pi-vv,-ww))-R)),      [uu,Pi-vv,-ww]];
	G[7]:= [MatrixNorm(evalf((rot(Pi-uu,vv,-ww))-R)),      [Pi-uu,vv,-ww]];
	G[8]:= [MatrixNorm(evalf((rot(Pi-uu,Pi-vv,-ww))-R)),   [Pi-uu,Pi-vv,-ww]];
	
	
	
	(op(sort({seq(G[i], i=1...8)}))[1])[2];
	
	
	
	#############################################################
	
