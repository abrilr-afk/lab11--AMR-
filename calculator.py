#https://github.com/abrilr-afk/lab11--AMR-.git
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
        print(f"Error: {e}")
        raise

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base of logarithm must be greater than 0 and not equal to 1.")

def exponent(a, b):
    return a ** b


