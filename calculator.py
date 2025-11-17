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
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")
        raise

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
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <- 0:
        raise ValueError("Logarithm argument must be greater than zero")
    return math.log(b, a)

def exp(a, b):
    return a ** b


