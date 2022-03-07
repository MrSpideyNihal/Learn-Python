"""Simple calculator."""
import math

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    while True:
        print("Enter an operation (+, -, *, /) or 'q' to quit.")
        op = input()
        if op.lower() == 'q':
            break
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            if op == '+':
                print(f"{a} + {b} = {add(a, b)}")
            elif op == '-':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif op == '*':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif op == '/':
                if b != 0:
                    print(f"{a} / {b} = {divide(a, b)}")
                else:
                    print("Error: Cannot divide by zero!")
        except ValueError as e:
            print(e)
