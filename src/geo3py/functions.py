"""
Raw mathematical functions. Most functions in this module are from the official course material, 2022_DGPD_NOTER.pdf
"""

from sympy import *
from .utils import *
from collections import namedtuple

# Definition 12.10, tangentplan
def get_N(r, u, v):
    """DGPD, def-12.10, tangentplan"""
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
    result = namedtuple('FrenetSerretVec', 'e f g')
    return result(e, f, g)

def get_Jacobi2(r, u, v):
    jac = diff(r, u).cross(diff(r, v)).norm()
    return simplify(jac)

def get_Jacobi3(r, u, v, w):
    jac = (diff(r, u).cross(diff(r, v))).dot(diff(r, w))
    return simplify(jac)

# 8.85, side 156
def get_Omega(R, t):
    Omega = simplify(diff(R, t)*(R.T))
    # omega = Matrix([Omega[1,2], Omega[2,0], Omega[0,1]])
    omega = Matrix([Omega[2,1], Omega[0,2], Omega[1,0]])
    return Omega, omega

def get_skrue_h(omega, p, t):
    pdiff = diff(p, t)
    h = simplify((omega.dot(pdiff)) / (omega.norm()**2))
    return h
