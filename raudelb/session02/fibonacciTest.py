__author__ = 'raudel'

import unittest
import series




class FibonacciTest(unittest.TestCase):

    def test_cero_fibonacci_returns_zero(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)

    

    def test_add_exception_val_returns_addition(self):
        try:
            calculator = StringCalculator()
            result = calculator.add('2,4,-2,2000,-8')
            self.assertEqual(result, 6)

        except ValueError as error:
            print(repr(error))

if __name__ == '__main__':
    unittest.main()