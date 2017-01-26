from unittest import TestCase


class TestSum_series(TestCase):

    def test_iter_fibonacci(self):
        from series import sum_series
        from series import Fibonacci

        fib = Fibonacci()
        sumSer = sum_series()

        for ii in range(25):
            self.assertEqual(fib.iter(ii), sumSer.iter(ii))
            self.assertEqual(fib.iter(ii), sumSer.iter(ii, 0, 1))



    def test_iter_lucas(self):
        from series import sum_series
        from series import Lucas

        luc = Lucas()
        sumSer = sum_series()

        for ii in range(25):
            self.assertEqual(luc.iter(ii), sumSer.iter(ii, 2, 1))



    def test_recurs_fibonacci(self):
        from series import sum_series
        from series import Fibonacci

        fib = Fibonacci()
        sumSer = sum_series()

        for ii in range(25):
            self.assertEqual(fib.recurs(ii), sumSer.recurs(ii))
            self.assertEqual(fib.recurs(ii), sumSer.recurs(ii, 0, 1))



    def test_recurs_Lucas(self):
        from series import sum_series
        from series import Lucas

        luc = Lucas()
        sumSer = sum_series()

        for ii in range(25):
            self.assertEqual(luc.recurs(ii), sumSer.recurs(ii, 2, 1))