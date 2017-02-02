from unittest import TestCase

class TestFibonacci(TestCase):

    def test_iter(self):
        from series import Fibonacci

        fib = Fibonacci()
        self.assertEqual(0, fib.iter(0))
        self.assertEqual(1, fib.iter(1))
        self.assertEqual(1, fib.iter(2))
        self.assertEqual(2, fib.iter(3))
        self.assertEqual(3, fib.iter(4))
        self.assertEqual(5, fib.iter(5))
        self.assertEqual(8, fib.iter(6))
        self.assertEqual(13, fib.iter(7))
        self.assertEqual(21, fib.iter(8))
        self.assertEqual(34, fib.iter(9))
        self.assertEqual(55, fib.iter(10))

    def test_recurs(self):
        from series import Fibonacci

        x_max = 25
        fib = Fibonacci()
        for ii in range(x_max + 1):
            self.assertEqual(fib.iter(ii), fib.recurs(ii))