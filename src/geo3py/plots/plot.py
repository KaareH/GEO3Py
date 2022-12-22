"""
This modules contains interactive plots.
Interactive with plotting-backends different from Matplotlib may not render in exported Jupyter-notebooks.
"""

# init
#%matplotlib widget
#%matplotlib inline
import numpy as np
from sympy import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from spb import plot3d_parametric_surface, plot3d_parametric_line, PB, MB, KB
#%matplotlib notebook
from IPython.display import display, Markdown, Latex


def plotSurfInteractive(r, dom_1, dom_2, showPlot=True):
    #colorF = lambdify([t, u], GaussK)

    plt1 = plot3d_parametric_surface(*r, dom_1, dom_2, "r", backend=PB,
        #rendering_kw={"alpha": 0.75},
        #color_func=colorF,
        use_cm=True,
        adaptive=False, wireframe=True, show=False
    )

    if showPlot:
            plt1.show()
            return None
            
    return plt1
    # Dette plot er interaktivt og bliver ikke vist i PDF

def plotCurveInteractive(p, dom_1, showPlot=True):
    #colorF = lambdify([t, u], GaussK)

    plt1 = plot3d_parametric_line(*p, dom_1, "p", backend=PB,
        #rendering_kw={"alpha": 0.75},
        #color_func=colorF,
        use_cm=True,
        adaptive=False, wireframe=True, show=False
    )

    if showPlot:
            plt1.show()
            return None
            
    return plt1
    # Dette plot er interaktivt og bliver ikke vist i PDF


    