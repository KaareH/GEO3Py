"""
Simple representaion of a tetraeder
"""

# Todo deformation

from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple

class Tetraeder:
    def __init__(self, O, a, b, c):
        self.O = O
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return f"{latex(self.O)}, {latex(self.a)}, {latex(self.b)},  {latex(self.c)}"

    def getMatrix(self):
        return Matrix([self.a, self.b, self.c]).T

    def getVol(self):
        return simplify(abs(self.getMatrix().det()/6))
