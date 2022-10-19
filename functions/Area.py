# GEO3, Python port
# Area
# functions/Area.py


# Calculates the area of surface patch r(Br) via EFG.
# Globals: 
# Locals:  efg, e,f,g, ArDif
# Parameters: r, Br
def Area(r, Br):
	
	
	   
	efg:= unapply(EFG(r, [u,v]), u,v);
	e:= (u,v)-> efg(u,v)[1];
	f:= (u,v)-> efg(u,v)[2];
	g:= (u,v)-> efg(u,v)[3];
	ArDif:= (u,v)-> simplify(sqrt(e(u,v)*g(u,v)-f(u,v)*f(u,v)));
	
	simplify(int(int(ArDif(u,v), u=Br[1]...Br[2]), v=Br[3]...Br[4]));
	
