from unittest import TestCase


class TestMyDate(TestCase):

    def test_init(self):
        from MyDate import MyDate, InvalidDateError
        from datetime import datetime
        try:
            this_date = MyDate(2018, 3, 5)
            self.fail("TestMyDate.test_init MyDate(2018, 3, 5)"
                      " should raise an error")
        except InvalidDateError as inv_date_err:
            bench_str = "InvalidDateError: " \
                        "MyDate(year, month, day, future_date=False)" \
                        " - date can't be in the future (date > now)"
            self.assertEqual(bench_str, str(inv_date_err))
        try:
            this_date = MyDate.from_datetime(datetime.now().date())
        except InvalidDateError:
            self.fail("TestMyDate.test_init "
                      "MyDate.from_datetime"
                      " shouldn't raise an exception")
        else:
            self.assertEqual(datetime.now().date(), this_date)

    def test_eq(self):
        from MyDate import MyDate
        date = MyDate(2014, 5, 23)
        self.assertEqual(MyDate(2014, 5, 23), date)
        self.assertNotEqual(date, MyDate(2014, 5, 24))
