from unittest import TestCase


class TestData:
    @staticmethod
    def bench_str() -> str:
        return \
            "M Miles Davis\n" \
            "154, boulevard Saint-Germain\n" \
            "75006 - Paris\n" \
            "France\n" \
            "+33 1 45 67 33 12\n" \
            "miles.davis@myself.com\n\n" \
            "Dear M Miles Davis,\n\n" \
            "Thank you very much for your donation.\n\n" \
            "Yours sincerely,\n\n" \
            "James Moody\n"


class TestEmailDonationsGenerator(TestCase):
    def test_write(self):

        from test_ReportDonationsDBGenerator import TestReportDonationsDBGenerator
        from EmailGenerator import EmailDonationsGenerator
        from PersonId import PersonId
        from Donation import Donation
        from Name import PersonName
        from datetime import date

        self.maxDiff = None

        db = TestReportDonationsDBGenerator._init_db()

        donor_id = PersonId(PersonName("M", "Miles", "Davis"), date(1926, 5, 26))
        donation = Donation(donor_id, date(2008, 1, 23), 5678.56)

        try:
            email_gen = EmailDonationsGenerator(db, donation, "James Moody")
            self.fail("Should generate an ValueError exception")
        except ValueError as ve:
            self.assertEqual("ValueError - "
                             "EmailDonationsGenerator(donations_db,"
                             " donor_id, donation_date):"
                             " donation not in database", str(ve))

            donation = Donation(donor_id, date(2011, 5, 19), 67000)
            email_gen = EmailDonationsGenerator(db, donation, "James Moody")
