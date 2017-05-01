from unittest import TestCase

#TODO: update

class TestBackToMenu(TestCase):
    def test_raise_BackToMenu(self):
        def __test_helper():
            from GoBackToHomeMenu import GoBackToHomeMenu
            try:
                raise GoBackToHomeMenu("GoBackToHomeMenu")
                self.fail('test_raise_BackToMenu()')
            except GoBackToHomeMenu as btm:
                self.assertEqual('GoBackToHomeMenu', str(btm))
                raise
                self.fail('test_raise_BackToMenu()')
        try:
            __test_helper()
            self.fail('test_raise_BackToMenu()')
        except Exception as exc:
            self.assertEqual('GoBackToHomeMenu', str(exc))