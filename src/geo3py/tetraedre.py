# Todo deformation

from .functions import *
from .utils import *
from sympy import *
from collections import namedtuple

class Tetraedre:
    def __init__(self, O, a, b, c):
        self.O = O
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return f"{latex(self.O)}, {latex(self.a)}, {latex(self.b)},  {latex(self.c)}"

    
