from unittest import TestCase


class TestInvalidUserChoice(TestCase):

    def test_instantiate(self):

        def __test_helper():
            from InvalidUserChoice import InvalidUserChoice
            try:
                raise InvalidUserChoice("test_instantiate() invalid argument")
                self.fail("Should raise an exception")
            except InvalidUserChoice as inv_uc:
                except_str = "test_instantiate() invalid argument"
                self.assertEqual(except_str, str(inv_uc))
                raise
        try:
            __test_helper()
            self.fail("Should raise exception (reraised in the function)")
        except ValueError as ve:
            except_str = "test_instantiate() invalid argument"
            self.assertEqual(except_str, str(ve))
