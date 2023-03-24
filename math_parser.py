"""Recursive descent math parser."""
import re

def tokenize(expression):
    """Tokenize the given expression into a list of tokens."""
    return [tok.group() for tok in re.finditer(r'[-+*/(). ]', expression)]

def parse(tokenized):
    """Parse the tokenized expression and evaluate it."""
    if not tokenized:
        return 0
    elif len(tokenized) == 1:
        return float(tokenized[0])
    else:
        operator = tokenized.pop(0)
        operand1 = parse(tokenized)
        if tokenized and tokenized[0] in '+-':
            tokenized.pop(0)
            operand2 = parse(tokenized)
            return eval(f'{operand1} {operator} {operand2}')
        else:
            return eval(f'{operand1} {operator}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python math_parser.py <expression>")
        sys.exit(1)
    expression = sys.argv[1]
    try:
        result = parse(tokenize(expression))
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
