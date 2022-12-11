# Todo rotaioner, skaleringer
# Todo SVD
# SVD for generelle matrix m x n

from sympy import Matrix, eye, cos, sin, simplify
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

# 4.1.4

def getRx(u):
    return Matrix([
        [1, 0, 0],
        [0, cos(u), -sin(u)],
        [0, sin(u), cos(u)],
    ])

def getRy(v):
    return Matrix([
        [cos(v), 0, -sin(v)],
        [0, 1, 0],
        [sin(v), 0, cos(v)]
    ])

def getRz(w):
    return Matrix([
        [cos(w), -sin(w), 0],
        [sin(w), cos(w), 0],
        [0, 0, 1]
    ])

def getRxyz(u, v, w):
    return simplify(getRx(u) * getRy(v) * getRz(w))

def getF():
    E = eye(3)
    return Matrix([E[1,:], E[0,:], E[2,:]])