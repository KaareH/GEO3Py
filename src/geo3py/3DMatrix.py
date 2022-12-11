# Todo rotaioner, skaleringer
# Todo SVD
# SVD for generelle matrix m x n

from sympy import Matrix, eye
from collections import namedtuple

# Sætning 4.29
def SVD3(K):
    U, S, V = K.singular_value_decomposition()
    E = eye(3)
    F_hat = E
    if K.det() < 0:
        E_flipped = E.tolist()
        #E_flipped.reverse()
        F_hat = Matrix([E_flipped[1], E_flipped[0], E_flipped[2]])
    elif K.det() == 0:
        raise Exception("Determinant is 0!")
    result = namedtuple('result', 'U S V F_hat')
    return result(U, S, V, F_hat)

