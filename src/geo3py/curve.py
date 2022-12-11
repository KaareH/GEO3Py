
from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple

    
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



