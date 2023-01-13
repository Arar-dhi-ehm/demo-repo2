"""
unit test module
    It will test every functionality of employee.py

"""

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    # This is called method or object
    def setUp(self):
        """Will run its code before every single test"""
        # Set below as instance attribute by using self.
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """Will run its code after every single test"""
        pass

    def test_email(self):
        # Check both emails from the expected values below.
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        # Try to change their first name
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        # Check both names from the expected values below.
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_full_name(self):
        # Check both names from the expected values below.
        self.assertEqual(self.emp_1.full_name, 'Corey Schafer')
        self.assertEqual(self.emp_2.full_name, 'Sue Smith')

        # Try to change their first name
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        # Check both names from the expected values below.
        self.assertEqual(self.emp_1.full_name, 'John Schafer')
        self.assertEqual(self.emp_2.full_name, 'Jane Smith')

    def test_apply_raise(self):
        # Apply the raise by 5%
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        # Check if the raise of 5% is correct
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
