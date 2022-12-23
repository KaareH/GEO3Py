"""
geo3py is a convienient Python library intended for use in DTU-course #01237 - Differentialgeometri og parametrisk design.

Website: https://github.com/KaareZ/GEO3Py

"""

import importlib.metadata
__version__ = importlib.metadata.version("geo3py")

from .core          import *
from .utils         import *
from .functions     import *
from .curve         import *
from .surface       import *
from .solid         import *
from .basistrekant  import *
from .tetraeder     import *
from .matrix2D      import *
from .matrix3D      import *
from .plots         import *
