from UserInputMenu import UserInputMenu


class ThankYouEmailMenu(UserInputMenu):
    from Database import Database
    from sys import stdin, stdout
    from PersonId import PersonId

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):
        from QuitMenu import QuitMenu
        from datetime import datetime

        super(ThankYouEmailMenu, self).__init__(donations_db, max_menu_calls,
                                                max_trials, istream, ostream)
        self._quit_menu = QuitMenu(donations_db=donations_db,
                                   max_menu_calls=max_menu_calls,
                                   max_trials=max_trials,
                                   istream=istream,
                                   ostream=ostream)
        self._name_menu = ["prefix", "first name", "last name",
                           "birth date year", "birth date month", "birth date day"]
        self._validate = [self._is_valid_prefix, self._is_valid_first_last_name, self._is_valid_first_last_name,
                          self._is_valid_birth_year, self._is_valid_birth_month, self._is_valid_birth_day]
        self._index = -1
        self._num_calls = -1
        self._max_calls = len(self._name_menu)
        self._now = datetime.now()
        self._prefix = None
        self._first_name = None
        self._last_name = None
        self._year = None
        self._month = None
        self._day = None
        self._input = [self._prefix, self._first_name, self._last_name, self._year, self._month, self._day]

    def _make_request_string(self) -> str:
        return "\nSending a thank you email to the donor [Q|q to quit]\n\n"

    def _make_menu_string(self) -> str:
        return "Please enter the donor's "

    def _update_menu(self) -> None:
        self._messages["menu"] = self._make_menu_string()

    def _do_continue(self) -> bool:
        if self._num_calls < self._max_calls:
            return True

    def _is_valid_input(self, input: str) -> bool:
        if self._num_calls == self._max_calls - 1:
            from PersonId import PersonId
            from Name import PersonName
            from datetime import date
            donor_name = PersonName(self._prefix, self._first_name, self._last_name)
            donation_date = date(self._year, self._month, self._day)
            return self.donations_db.donor_exists(PersonId(donor_name, donation_date))
        return self._validate[self._index](input)

    def _record_input(self, input: str) -> None:
        self._input[self._index] = input

    def _create_donor_id(self) -> PersonId:
        from PersonId import PersonId
        from Name import PersonName
        from datetime import date
        return PersonId(PersonName(self._prefix, self._first_name, self._last_name),
                        date(self._year, self._month, self._day))

    @staticmethod
    def _is_valid_prefix(prefix: str) -> bool:
        return prefix in ("M", "Ms")

    def _is_valid_first_last_name(self, name_comp: str) -> bool:
        # TODO: update
        return True

    # TODO: create a IsValidDate class
    def _is_valid_birth_year(self, year_str: str) -> bool:
        year = int(year_str)
        return year > 1800 and year < self._now.year

    def _is_valid_birth_month(self, month_str) -> bool:
        month = int(month_str)
        if self._year == self._now.year:
            return month > 0 and month <= self._now.month
        return month > 0 and month <= 12

    def _is_valid_birth_day(self, day_str: bool) -> bool:
        # TODO: add months array and is_leap_year function
        day = int(day_str)
        if self._year == self._now.year and self._month == self._now.month:
            return day > 0 and day <= self._now.day
        return day > 0 and day <= 31

    def _increment_counter(self):
        self._index += 1
        self._num_calls += 1

    def _print_request_and_menu(self) -> str:
        from Utilities import Utilities
        self._increment_counter()
        return Utilities.request(self.ostream,
                                 self.istream,
                                 self.messages["request"] +
                                 self.messages["menu"] +
                                 self._name_menu[self._index] + "\n" +
                                 self.messages["input"])

    def _is_valid_donor_id(self, donor_id: str) -> bool:
        return self._donations_db.donor_exists(donor_id)
