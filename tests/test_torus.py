from sympy import symbols, Matrix, cos, pi, sin
from geo3py.surface import Surface3D

def test_get_surface_area():
    u, v, t = symbols('u v t', real=True)
    r = Matrix([2*cos(t)+cos(t)*cos(u), 2*sin(t)+sin(t)*cos(u), sin(u)])
    t_dom = (t, 0, 2*pi)
    u_dom = (u, -pi, pi)
    torus_surf = Surface3D("r(t,u)", r, t_dom, u_dom)

    area, details = torus_surf.getArea()

    assert area == 8*pi**2

def test_success():
    #test = True
    assert True
