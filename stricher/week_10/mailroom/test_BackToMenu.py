from unittest import TestCase

#TODO: update

class TestBackToMenu(TestCase):
    def test_raise_BackToMenu(self):
        def __test_helper():
            from BackToMenu import BackToMenu
            try:
                raise BackToMenu("BackToMenu")
                self.fail('test_raise_BackToMenu()')
            except BackToMenu as btm:
                self.assertEqual('BackToMenu', str(btm))
                raise
                self.fail('test_raise_BackToMenu()')
        try:
            __test_helper()
            self.fail('test_raise_BackToMenu()')
        except Exception as exc:
            self.assertEqual('BackToMenu', str(exc))