
from MenuActions import MenuActions


class ThankYouEmailMenuActions(MenuActions):
    from io import IOBase
    from Database import Database
    from Donation import Donation
    from PersonId import PersonId

    def __init__(self, donations_db: Database, ostream: IOBase,
                 donation: Donation,
                 organisation_member_id: PersonId):
        super(ThankYouEmailMenuActions, self).__init__(donations_db, ostream)
        self._donation = donation
        self._organisation_member_id = organisation_member_id

    def send_a_thank_you_email(self):
        from BenchData import TestThat
        test_that = TestThat()
        if test_that.do():
            self._ostream.write(
                test_that.get_trace("ThankYouEmailMenuActions.send_a_thank_you_email")
            )
        else:
            from EmailGenerator import EmailDonationsGenerator
            email_gen = EmailDonationsGenerator(self.donations_db,
                                                self._donation,
                                                self._organisation_member_id)
            email_gen.write(self._ostream)
