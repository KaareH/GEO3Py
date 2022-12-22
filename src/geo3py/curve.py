"""
Represent parametric curves in 3D space. Convenient common functions
"""

from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple
from spb import plot3d_parametric_line, PB, MB, KB
from numpy import ptp, array, min, max

class Curve3D:
    def __init__(self, p, t_dom):
        self.p = p
        self.t_dom = t_dom
        
    def __str__(self):
        return f"{latex(self.p)}, {domain_latex(self.t_dom)}"

    def getKappa(self):
        return get_kappa(self.p, self.t_dom[0])

    def getTau(self):
        return get_tau(self.p, self.t_dom[0])
    
    def getFrenetSerret(self):
        return get_FrenetSerret(self.p, self.t_dom[0])


    def quickPlot(self, showPlot=True):
        plt1 = plot3d_parametric_line(*self.p, self.t_dom, backend=MB, rendering_kw={}, use_cm=False, show=False)
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

