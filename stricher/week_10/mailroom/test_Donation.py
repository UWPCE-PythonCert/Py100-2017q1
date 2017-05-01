from unittest import TestCase


class TestDonation(TestCase):

    def test_Donation(self):

        from Donation import Donation
        from BenchData import DonorsDBBenchData
        from PersonId import PersonId
        from EmailAddress import EmailAddress
        from MyDate import MyDate

        donors = DonorsDBBenchData().data

        donor1 = donors[PersonId(EmailAddress(
            "charles.ives@centralparkinthedark.com"
        )).value]
        donor_str = 'M Charles Ives\n' \
                    '14, Avenue Foch\n75016 - Paris\n' \
                    'France\n' \
                    '+33 1 45 67 83 45\n' \
                    'charles.ives@centralparkinthedark.com\n'
        self.assertEqual(donor_str, str(donor1))
        donation = Donation(donor1, MyDate(2012, 4, 12), 567)
        donation_str = "\nDonor:\n------\nM Charles Ives\n14, Avenue Foch\n" \
                       "75016 - Paris\nFrance\n+33 1 45 67 83 45\n" \
                       "charles.ives@centralparkinthedark.com\n\n" \
                       "Donation:\n---------\n2012-04-12: 567"
        self.assertEqual(donation_str, str(donation))
        self.assertEqual(PersonId(EmailAddress(donation.donor.mail.get)), donation.donor.id)
        self.assertEqual(PersonId(EmailAddress(donation.donor.mail.get)).value, donation.donor.id.value)

    def test_equality(self):

        from BenchData import DonorsDBBenchData
        from PersonId import PersonId
        from EmailAddress import EmailAddress

        donors = DonorsDBBenchData().data
        donor1 = donors[PersonId(EmailAddress(
            "charles.ives@centralparkinthedark.com"
        )).value]
        donor2 = donors[PersonId(EmailAddress("lee.morgan@jazzmessengers.com")).value]
        self.assertEqual(donor1, donor1)
        self.assertNotEqual(donor1, donor2)
        self.assertEqual(donor2, donor2)