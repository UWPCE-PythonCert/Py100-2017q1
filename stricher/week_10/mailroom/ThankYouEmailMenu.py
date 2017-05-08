from UserInputMenu import UserInputMenu

#TODO: Work on ThankYouEmailMenu

class ThankYouEmailMenu(UserInputMenu):
    from Database import Database
    from sys import stdin, stdout

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):
        from datetime import datetime
        super(ThankYouEmailMenu, self).__init__(donations_db, max_menu_calls,
                                                max_trials, istream, ostream)
        self._name_menu = ["Email:",
                           "birth date [YYYY-mm-dd]",
                           "donation date [YYYY-mm-dd]",
                           "donation amount"]
        self._max_calls = len(self._name_menu)
        self._now = datetime.now()
        self._donor_email = None
        self._donation_date = None
        self._donation_amount = None
        self._donor_id = None
        self._organisation_member = None
        self._thank_you_email_actions = None

    def _make_request_string(self) -> str:
        return "\nSending a thank you email " \
               "to the donor {}\n\n". \
            format(super(ThankYouEmailMenu, self).
                   _make_request_string())

    def _make_menu_string(self) -> str:
        return "Please enter the " + ("donor's " if self._index <= 1 else "donations's ")

    def _update_menu(self) -> None:
        self._messages["menu"] = self._make_menu_string()

    def _do_continue(self) -> bool:
        if self._num_calls < self._max_calls:
            return True

    def _end_input(self) -> bool:
        return self._num_calls == self._max_calls - 1

    def _valid_and_record_email(self, input: str) -> bool:
        from EmailAddress import EmailAddress, EmailAddressError
        try:
            self._donor_email = EmailAddress(input)
        except EmailAddressError:
            return False
        else:
            return True

    def _valid_and_record_donor_id(self) -> bool:
        from PersonId import PersonId
        person_id = PersonId(self._donor_email)
        if self.donations_db.donor_exists(person_id.value):
            self._donor_id = person_id
            return True
        return False

    def _valid_and_record_donation_date(self, input: str) -> bool:
        from MyDate import MyDate, InvalidDateError
        try:
            self._donation_date = MyDate.from_string(input)
        except InvalidDateError:
            return False
        else:
            return True

    def _valid_and_record_donation_amount(self, amount: str) -> bool:
        try:
            amount = float(amount)
        except ValueError:
            return False
        else:
            if amount >= 0:
                self._donation_amount = amount
                return True
            return False

    def _valid_and_record_donation(self) -> bool:
        from Donation import Donation
        donation = Donation(self._donor_id, self._donation_date,
                            self._donation_amount)
        if self.donations_db.donation_exists(donation):
            self._donation = donation
            return True
        return False

    def _is_valid_input(self, input: str) -> bool:
        if self._index == 0:
            return self._valid_and_record_email(input) and \
                   self._valid_and_record_donor_id()
        if self._index == 1:
            return self._valid_and_record_donation_date(input)
        if self._index == 2:
            return self._valid_and_record_donation_amount(input) and \
                   self._valid_and_record_donation()

    def _print_request_and_menu(self) -> str:
        from Utilities import Utilities
        return Utilities.request(self.ostream,
                                 self.istream,
                                 self.messages["request"] +
                                 self.messages["menu"] +
                                 self._name_menu[self._index] + "\n" +
                                 self.messages["input"])

    def _process(self):
        from ThankYouEmailMenuActions import ThankYouEmailMenuActions
        thank_you_email = ThankYouEmailMenuActions(self.donations_db)
        # TODO: complete
