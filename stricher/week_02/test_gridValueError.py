from unittest import TestCase

class TestGridValueError(TestCase):

    def test_raise_(self):
        from GridValueError import GridValueError
        try:
            raise GridValueError("Grid() - Invalid args")
        except GridValueError as gve:
            self.assertEqual("Grid() - Invalid args", str(gve))
        except:
            self.fail()