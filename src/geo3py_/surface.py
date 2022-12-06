#__all__ = ["Surface3D"]

from sympy import *
from .utils import *
from collections import namedtuple

class Surface3D:
    def __init__(self, name, r, dom_1, dom_2):
        self.name = name
        self.r = r
        self.dom_1 = dom_1
        self.dom_2 = dom_2
        
    def __str__(self):
        return f"{self.name} = {latex(self.r)}, {domain_latex(self.dom_1)}, {domain_latex(self.dom_2)}"

    def getJacobi(self):
        symbol_1 = self.dom_1[0]
        symbol_2 = self.dom_2[0]
        jacobi = diff(self.r, symbol_1).cross(diff(self.r, symbol_2)).norm()
        return simplify(jacobi)
        
    def getArea(self, dom_1=None, dom_2=None):
        if dom_1 is None: dom_1 = self.dom_1
        if dom_2 is None: dom_2 = self.dom_2
        jacobi = self.getJacobi()

        area_int = simplify(Integral(jacobi, dom_1, dom_2))
        area = area_int.doit()

        Details = namedtuple('details', 'jacobi integrand dom_1 dom_2')
        return area, Details(jacobi, area_int, dom_1, dom_2)
    
    def __getDefInfo(self):
        return self.r, self.dom_1[0], self.dom_2[0]

    def getN(self):
        return get_N(*self.__getDefInfo())
    
    def getF_I(self):
        return get_F_I(*self.__getDefInfo())
    
    def getF_II(self):
        return get_F_II(*self.__getDefInfo())

    def getWeingarten(self):
        return get_Weingarten(*self.__getDefInfo())

    def getGaussK(self):
        return get_GaussK(self.getWeingarten())
    
    def getMiddelH(self):
        return get_MiddelH(self.getWeingarten())

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
        


