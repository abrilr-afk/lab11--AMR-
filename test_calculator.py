#https://github.com/abrilr-afk/lab11--AMR-.git
#Partner 1: Abril Rodriguez
#Partner 2: Abril Rodriguez
import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(-2, -4), -6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(3, -2), 5)
        self.assertEqual(subtract(-2, 3), -5)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
         self.assertEqual(mul(2, 3), 6)
         self.assertEqual(mul(4, 2), 8)
         self.assertEqual(mul(3, 4), 12)

    def test_divide(self): # 3 assertions
         self.assertEqual(div(2, 4), 2)
         self.assertEqual(div(2, 10), 5)
         self.assertEqual(div(3, 9), 3)


######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 9)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(3, 4), 1.261860, places=6)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(2, 4), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 3)
        with self.assertRaises(ValueError):
            logarithm(0, 4)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -8)
        with self.assertRaises(ValueError):
            logarithm(4, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 5), 5)
        self.assertAlmostEqual(hypotenuse(5, 5), math.sqrt(50), places=7)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(25), 5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()