from unittest import TestCase


class TestLucas(TestCase):
    def test_iter(self):
        from series import Lucas

        luc = Lucas()
        self.assertEqual(2, luc.iter(0))
        self.assertEqual(1, luc.iter(1))
        self.assertEqual(3, luc.iter(2))
        self.assertEqual(4, luc.iter(3))
        self.assertEqual(7, luc.iter(4))
        self.assertEqual(11, luc.iter(5))
        self.assertEqual(18, luc.iter(6))
        self.assertEqual(29, luc.iter(7))

    def test_recurs(self):
        from series import Lucas

        n_max = 25
        luc = Lucas()
        for ii in range(n_max + 1):
            self.assertEqual(luc.iter(ii), luc.recurs(ii))