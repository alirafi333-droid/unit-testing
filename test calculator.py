import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("Setting up...")
        self.calc = calculator()

    def tearDown(self):
        print("Cleaning up...")
        del self.calc

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)