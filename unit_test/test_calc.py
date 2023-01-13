"""
unit test module
    It will test every functionality of calc.py

Create test cases for the functions that we want to test. In order to create those test cases.
We need to create a test class first that inherits from unittest.testcase.
To do this, create a class named class TestCalc(unittest.TestCase)
Inheriting from 'unittest.TestCase' will give us access to a lot of testing capabilities within that class
"""

import unittest
import calc


class TestCalc(unittest.TestCase):

    # # Name a method
    # def test_add(self):
    #     result = calc.add(10, 5)
    #     # Test this by checking if result is equal to 15
    #     self.assertEqual(result, 14)

    def test_add(self):
        # (result, expected_test_result)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        # (result, expected_test_result)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # (result, expected_test_result)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        # (result, expected_test_result)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)



if __name__ == '__main__':
    unittest.main()


