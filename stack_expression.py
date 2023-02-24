"""Evaluate postfix expressions using a stack."""
import operator

def apply_operator(operator, stack):
    """Apply binary operator to top two elements of the stack."""
    if len(stack) < 2:
        raise ValueError("Invalid stack size")
    b = stack.pop()
    a = stack.pop()
    return operator(a, b)

if __name__ == "__main__":
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    print(apply_operator(ops['*'], [1, 2]))
