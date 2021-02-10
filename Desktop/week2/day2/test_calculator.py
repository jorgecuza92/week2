from calculator import Calculator
import unittest


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    def test_add_numbers(self):
        
        result = self.calculator.add(5,5)
        self.assertEqual(10, result)

    def test_multiply_numbers(self):
        self.assertEqual(15, self.calculator.multiply(3,5))


unittest.main()