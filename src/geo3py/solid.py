from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple
from spb import plot3d_parametric_surface, PB, MB, KB
from numpy import ptp, array, min, max, linspace
import matplotlib.pyplot as plt

class Solid3D:
    def __init__(self, name, r, dom_1, dom_2, dom_3):
        self.name = name
        self.r = r
        self.dom_1 = dom_1
        self.dom_2 = dom_2
        self.dom_3 = dom_3
        
    def __str__(self):
        return f"{self.name} = {latex(self.r)}, {domain_latex(self.dom_1)}, {domain_latex(self.dom_2)}, {domain_latex(self.dom_3)}"

    def getJacobi(self):
        symbol_1 = self.dom_1[0]
        symbol_2 = self.dom_2[0]
        symbol_3 = self.dom_3[0]
        jacobi = get_Jacobi3(self.r, symbol_1, symbol_2, symbol_3)
        return jacobi

    def getVolume(self, dom_1=None, dom_2=None, dom_3=None):
        if dom_1 is None: dom_1 = self.dom_1
        if dom_2 is None: dom_2 = self.dom_2
        if dom_3 is None: dom_3 = self.dom_3
        jacobi = self.getJacobi()

        vol_int = simplify(Integral(jacobi, dom_1, dom_2, dom_3))
        vol = simplify(vol_int.doit())

        details = namedtuple('details', 'jacobi integrand dom_1 dom_2 dom_3')
        return vol, details(jacobi, vol_int, dom_1, dom_2, dom_3)

    def quickPlot(self, showPlot=True, COUNT_1 = 5, COUNT_2 = 5, COUNT_3 = 5):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        xs = zeros(COUNT_1*COUNT_2*COUNT_3)
        ys = zeros(COUNT_1*COUNT_2*COUNT_3)
        zs = zeros(COUNT_1*COUNT_2*COUNT_3)

        t_s = linspace(float(self.dom_1[1]), float(self.dom_1[2]), COUNT_1)
        u_s = linspace(float(self.dom_2[1]), float(self.dom_2[2]), COUNT_2)
        w_s = linspace(float(self.dom_3[1]), float(self.dom_3[2]), COUNT_3)

        for i in range(COUNT_1):
            for j in range(COUNT_2):
                for k in range(COUNT_3):
                    index = i*COUNT_2*COUNT_3 + j*COUNT_3 + k
                    xyz = (self.r.subs({self.dom_1[0]: t_s[i], self.dom_2[0]:u_s[j], self.dom_3:w_s[k]})).evalf()
                    xs[index] = xyz[0]
                    ys[index] = xyz[1]
                    zs[index] = xyz[2]

        ax.scatter3D(xs, ys, zs)

        ranges = array([ptp(xs), ptp(ys), ptp(zs)])
        max_range = max(ranges)

        x_ratio = max_range/ranges[0]
        y_ratio = max_range/ranges[1]
        z_ratio = max_range/ranges[2]

        ax.set_xlim(min(xs) * x_ratio, max(xs) * x_ratio)
        ax.set_ylim(min(ys) * y_ratio, max(ys) * y_ratio)
        ax.set_zlim(min(zs) * z_ratio, max(zs) * z_ratio)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        if showPlot:
            fig.show()
            return None
            
        return fig

