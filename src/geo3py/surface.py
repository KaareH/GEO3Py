#__all__ = ["Surface3D"]

from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple
from spb import plot3d_parametric_surface, PB, MB, KB
from numpy import ptp, array, min, max

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
        jacobi = get_Jacobi2(self.r, symbol_1, symbol_2)
        return simplify(jacobi)
        
    def getArea(self, dom_1=None, dom_2=None):
        # Brug objektets interval eller det der bliver givet
        if dom_1 is None: dom_1 = self.dom_1
        if dom_2 is None: dom_2 = self.dom_2
        jacobi = self.getJacobi()

        area_int = simplify(Integral(jacobi, dom_1, dom_2))
        area = simplify(area_int.doit())

        details = namedtuple('details', 'area jacobi integrand dom_1 dom_2')
        return area, details(
            Eq(Symbol('A'), area),
            Eq(Symbol('Jacobi'), jacobi),
            Eq(Symbol('A'), area_int),
            dom_1,
            dom_2)
    
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

    def quickPlot(self, showPlot=True):
        plt1 = plot3d_parametric_surface(*self.r, self.dom_1, self.dom_2, backend=MB, rendering_kw={"alpha": 0.8}, wireframe=True, use_cm=False, show=False)
        xs = plt1[0].get_data()[0]
        ys = plt1[0].get_data()[1]
        zs = plt1[0].get_data()[2]

        ranges = array([ptp(xs), ptp(ys), ptp(zs)])
        max_range = max(ranges)

        x_ratio = max_range/ranges[0]
        y_ratio = max_range/ranges[1]
        z_ratio = max_range/ranges[2]

        plt1.xlim = (min(xs) * x_ratio, max(xs) * x_ratio)
        plt1.ylim = (min(ys) * y_ratio, max(ys) * y_ratio)
        plt1.zlim = (min(zs) * z_ratio, max(zs) * z_ratio)

        if showPlot:
            plt1.show()
            return None
            
        return plt1

