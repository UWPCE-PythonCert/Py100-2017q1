from datetime import date


class InvalidDateError(ValueError):
    def __init__(self, message: str):
        super(InvalidDateError, self).__init__("InvalidDateError: {}".format(message))


class MyDate(date):

    def __new__(cls, year: int, month: int, day: int, future_date=False):
        from datetime import datetime
        if not future_date and (date(year, month, day) > datetime.now().date()):
            raise InvalidDateError("MyDate(year, month, day,"
                                   " future_date=False) - "
                                   "date can't be in the future (date > now)")
        instance = super(MyDate, cls).__new__(cls, year, month, day)
        instance._future_date = future_date
        return instance

    @classmethod
    def from_datetime(cls, the_date, future_date=False):
        return MyDate(the_date.year, the_date.month, the_date.day, future_date)

    @property
    def future_date(self):
        return self._future_date

    @classmethod
    def from_string(cls, date_str: str):
        splitted = date_str.split("-")
        if len(splitted) != 3:
            raise InvalidDateError("InvalidDateError: MyDate.from_string(date_str)"
                                   " - Argument must be formatted as YYYY-MM-DD")
        try:
            year = int(splitted[0])
            month = int(splitted[1])
            day = int(splitted[2])
        except ValueError:
            raise InvalidDateError("InvalidDateError: MyDate.from_string(date_str)"
                                   " - Invalid string format")
        return cls(int(splitted[0]), int(splitted[1]),
                   int(splitted[2]), future_date=False)
