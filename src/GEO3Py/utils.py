# Display equation
def EqPrint(lhs, rhs):
    return Markdown(f"${lhs} = "f"{latex(rhs)}$")