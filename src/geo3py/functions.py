from sympy import *
from .utils import *
from collections import namedtuple

# Definition 12.10, tangentplan
def get_N(r, u, v):
    rxr = diff(r, u).cross(diff(r, v))
    return rxr / rxr.norm()

# Definition 13.1
def get_F_I(r, u, v):
    m = Matrix([[diff(r,u).dot(diff(r,u)), diff(r,u).dot(diff(r,v))],
                [diff(r,v).dot(diff(r,u)), diff(r,v).dot(diff(r,v))]])
    return m

# Definition 13.1
def get_F_II(r, u, v):
    r_N = get_N(r, u, v)
    m = Matrix([[diff(r,u,u).dot(r_N), diff(r,u,v).dot(r_N)],
                [diff(r,v,u).dot(r_N), diff(r,v,v).dot(r_N)]])
    return m

# Definition 13.6
def get_Weingarten(r, u, v):
    F_I = simplify(get_F_I(r, u, v))
    F_II = simplify(get_F_II(r, u, v))
    return simplify(F_I.inverse() * F_II)

# Definition 14.1
#def get_GaussK(kappa1, kappa2, u, v):
#    return

# Definition 14.3, 14.1
def get_GaussK(Weingarten):
    return Weingarten.det()

# Definition 14.3, 14.1
def get_MiddelH(Weingarten):
    return Weingarten.trace() / 2

# Sætning mangler
def get_v(p, t):
    return simplify(diff(p, t).norm())

# Sætning 8.25, kruming
def get_kappa(p, t, v = None):
    if v == None:
        v = get_v(p, t)

    kappa = simplify(((diff(p, t).cross(diff(p, t, t))).norm()) / (v**3))
    return kappa

# Sætning 8.25, torsion
def get_tau(p, t):
    torsion = simplify((diff(p, t).cross(diff(p, t, t)).dot(diff(p, t, t, t)))
        / ((diff(p, t).cross(diff(p, t, t))).norm()**2))
    return torsion

# Sætning 8.25, Frenet-Serret
def get_FrenetSerret(p, t):
    v = get_v(p, t)
    pm = diff(p, t)
    pmm = diff(p, t, t)
    e = simplify(pm/v)
    g = simplify((pm.cross(pmm)) / ((pm.cross(pmm)).norm()))
    f = simplify(g.cross(e))
    result = namedtuple('Frenet-Serret vec', 'e f g')
    return result(e, f, g)

def get_Jacobi2(r, u, v):
    jac = diff(r, u).cross(diff(r, v)).norm()
    return simplify(jac)
