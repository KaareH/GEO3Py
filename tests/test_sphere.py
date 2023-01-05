from sympy import symbols, pi, cos, sin, Matrix, simplify, Rational
from geo3py.surface import Surface3D
from geo3py.solid import Solid3D

from sympy import init_printing, pprint
init_printing() 

def test_sphere_area():
    u, v, R = symbols('u v R', real=True)
    r = Matrix([
        R*sin(u)*cos(v),
        R*sin(u)*sin(v),
        R*cos(u),
    ])
    u_dom = (u, 0, pi)
    v_dom = (v, 0, 2*pi)
    surf = Surface3D("r(u,v)", r, u_dom, v_dom)

    area, _ = surf.getArea()
    pprint(area)

    assert area == 4*pi*R**2

def test_sphere_volume():
    u, v, w, R = symbols('u v w R', real=True)
    r = Matrix([
        R*sin(u)*cos(v),
        R*sin(u)*sin(v),
        w*R*cos(u),
    ])
    u_dom = (u, 0, pi)
    v_dom = (v, 0, 2*pi)
    w_dom = (w, 0, 1)
    solid = Solid3D("r(u,v,w)", r, u_dom, v_dom, w_dom)

    volume, details = solid.getVolume(u_dom, v_dom, w_dom)
    pprint(volume)
    
    for detail in details:
        pprint(detail)
    
    expected_volume = Rational(4,3)*pi*R**3
    pprint(expected_volume)

    assert simplify(volume) == simplify(expected_volume)
    