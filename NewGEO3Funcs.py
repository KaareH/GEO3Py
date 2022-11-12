def EqPrint(lhs, rhs):
    return Markdown(f"${lhs} = "f"{latex(rhs)}$")

# Definition 12.10, tangentplan
def get_N(r, u, v):
    rxr = diff(r, u).cross(diff(r, v))
    return rxr / rxr.norm()

# Definition 13.1
def get_F_I(r, u, v):
    m = Matrix([[diff(r,u).dot(diff(r,u)), diff(r,u).dot(diff(r,v))]
        ,[diff(r,v).dot(diff(r,u)), diff(r,v).dot(diff(r,v))]])
    return m

# Definition 13.1
def get_F_II(r, u, v):
    r_N = get_N(r, u, v)
    m = Matrix([[diff(r,u,u).dot(r_N), diff(r,u,v).dot(r_N)]
        ,[diff(r,v,u).dot(r_N), diff(r,v,v).dot(r_N)]])
    return m

def get_Weingarten(r, u, v):
    F_I = simplify(get_F_I(r, u, v))
    F_II = simplify(get_F_II(r, u, v))
    return simplify(F_I.inverse() * F_II)

# Definition 14.1
#def get_GaussK(kappa1, kappa2, u, v):
#    return

# Definition 14.3
def get_GaussK(Weingarten):
    return Weingarten.det()

# Definition 14.3
def get_MiddelH(Weingarten):
    return Weingarten.trace() / 2