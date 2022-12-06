from sympy import *

# # Display equation
# def EqPrint(lhs, rhs):
#     return Markdown(f"${lhs} = "f"{latex(rhs)}$")

def testUtil():
    print("TestUtil func!")

def domain_latex(domain):
    symb = domain[0]
    lower = domain[1]
    upper = domain[2]
    return f"{symb} \in [{latex(lower)}, {latex(upper)}]"