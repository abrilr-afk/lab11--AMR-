#https://github.com/abrilr-afk/lab11--AMR-.git
#Partner 1: Abril Rodriguez
#Partner 2: Abril Rodriguez
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    try:
        if a < 0:
            raise ValueError("A can't be negative")
        return math.sqrt(a)
    except ValueError as e:
        raise ValueError(f"Error: {str(e)}") from None

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Base of logarithm must be greater than 0 and not equal to 1.")
    if b <- 0:
        raise ValueError("Logarithm argument must be greater than zero")
    return math.log(b, a)

def exp(a, b):
    return a ** b


