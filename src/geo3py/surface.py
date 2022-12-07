#__all__ = ["Surface3D"]

from functions import *
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
        # Brug objektets interval eller det der bliver givet
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

