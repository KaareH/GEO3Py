from sympy import symbols, Matrix, cos, pi, sin, asinh, sqrt, evalf, det, Rational, pprint
from geo3py.surface import Surface3D
from geo3py.solid import Solid3D
from geo3py.tetraeder import Tetraeder
from geo3py.matrix3D import SVD3

from sympy import init_printing, pprint
init_printing() 

def test_exam_E11_1(): # Standard tetraeder deformering
    tet1 = Tetraeder(
         [0,0,0],
         [1,0,0],
         [0,1,0],
         [0,0,1]
    )

    tet2 = Tetraeder(
        [0,0,0],
        [1,1,0],
        [1,0,1],
        [0,1,1]
    )

    # Del 1 - orientering af tet2 skal være negativ
    assert tet2.getMatrix().det() < 0

    # Del 2 - volumen
    assert tet2.getVol() == Rational(1,3)

    # Del 3 - bestem K
    K = tet2.getMatrix()
    print("K")
    pprint(K)
    assert K == Matrix([[1,1,0],[1,0,1],[0,1,1]])

    # Del 4 - bestem Sigma og F
    result = SVD3(K)
    expected_Sigma = Matrix([[2,0,0], [0,1,0], [0,0,1]])
    
    print("Sigma")
    pprint(result.S)
    print("Expected Sigma")
    pprint(expected_Sigma)

    assert result.S == expected_Sigma

    expected_F = Matrix([[0,1,0],[1,0,0],[0,0,1]])
    assert result.F_hat == expected_F

    