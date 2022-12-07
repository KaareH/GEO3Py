from sympy import symbols, Matrix, cos, pi, sin, asinh, sqrt, evalf
from src.geo3py.surface import Surface3D
from src.geo3py.solid import Solid3D

def test_exam_E21_3_3(): # Bestem areal af P2
    u, v, t = symbols('u v t', real=True)
    r = Matrix([cos(v) * (u + 5), sin(v) * (u + 5), -u ** 2 + 1])

    u_dom = (u, -1, 1)
    v_dom = (v, 0, 2*pi)
    surf = Surface3D("r(u,v)", r, u_dom, v_dom)

    area, details = surf.getArea()
    
    expected_area = 10*pi*sqrt(5) + 5*pi*asinh(2)
    assert area.equals(expected_area)

def test_exam_E21_3_4(): # Bestem volumen af P2
    u, v, w = symbols('u v w', real=True)
    r = Matrix([cos(v)*(5 + u), sin(v)*(5 + u), w*(-u**2 + 1)])

    u_dom = (u, -1, 1)
    v_dom = (v, 0, 2*pi)
    w_dom = (w, 0, 1)
    solid = Solid3D("r(u,v,w)", r, u_dom, v_dom, w_dom)

    vol, details = solid.getVolume()
    
    expected_vol = 40/3*pi
    assert vol.equals(expected_vol)

