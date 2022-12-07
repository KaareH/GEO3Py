from sympy import symbols, Matrix, cos, pi, sin, asinh, sqrt, evalf
from src.geo3py.surface import Surface3D

def test_exam_E21_3_3(): # Bestem areal af P2
    u, v, t = symbols('u v t', real=True)
    r = Matrix([cos(v) * (u + 5), sin(v) * (u + 5), -u ** 2 + 1])

    u_dom = (u, -1, 1)
    v_dom = (v, 0, 2*pi)
    surf = Surface3D("r(u,v)", r, u_dom, v_dom)

    area, details = surf.getArea()
    
    expected_area = 10*pi*sqrt(5) + 5*pi*asinh(2)
    assert area.equals(expected_area)

# def test_exam_E21_3_4(): # Bestem volumen af P2
#     u, v, t = symbols('u v t', real=True)
#     r = Matrix([cos(v) * (u + 5), sin(v) * (u + 5), -u ** 2 + 1])

#     u_dom = (u, -1, 1)
#     v_dom = (v, 0, 2*pi)
#     surf = Surface3D("r(u,v)", r, u_dom, v_dom)

#     vol, details = surf.getArea()
    
#     expected_vol = 40/3*pi
#     assert vol.equals(expected_vol)