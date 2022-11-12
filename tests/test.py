import NewGEO3Funcs as GEO3
from sympy import *
print("Test")


r = Matrix([2*cos(t)+cos(t)*cos(u), 2*sin(t)+sin(t)*cos(u), sin(u)])
t_dom = (t, 0, 2*pi)
u_dom = (u, -pi, pi)

u, v, t = symbols('u v t', real=True)
#u, v, t = symbols('u v t')
x, y, z = symbols('x y z')
a, b, c = symbols('a b c')

#GEO3.get_N