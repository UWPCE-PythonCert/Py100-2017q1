from unittest import TestCase


class DonationBenchData:

    def __init__(self):
        from datetime import date
        from Name import PersonName
        from PersonId import PersonId
        self.__data = \
            (
                dict(id=PersonId(PersonName("M", "Charles", "Ives"), date(1874, 10, 20)),
                     date=date(1950, 3, 28), amount=345.78),
                dict(id=PersonId(PersonName("M", "John", "Coltrane"), date(1930, 3, 22)),
                     date=date(1962, 5, 13), amount=4567.45),
                dict(id=PersonId(PersonName("M", "Duke", "Ellington"), date(1910, 4, 23)),
                     date=date(1965, 4, 24), amount=456.67)
            )

    @property
    def data(self):
        return self.__data


class TestDonation(TestCase):

    def test_Donation(self):

        from Donation import Donation

        bench = DonationBenchData()
        bench_data = bench.data

        for data in bench_data:

            donor_id = data["id"]
            donation_date = data["date"]
            donation_amount = data["amount"]

            donation = Donation(donor_id, donation_date, donation_amount)

            self.assertEqual(donation.donor_id, donor_id)

            id_str = donor_id.value
            self.assertEqual(id_str, donation.donor_id.value)

            self.assertEqual(donation_date, donation.date)
            self.assertEqual(donation_amount, donation.amount)

    def test_equality(self):

        from Donation import Donation
        from Donor import Donor

        bench = DonationBenchData()
        bench_data = bench.data

        for data in bench_data:
            donor_id = data["id"]
            donation_date = data["date"]
            donation_amount = data["amount"]

            donation1 = Donation(donor_id, donation_date, donation_amount)
            donation2 = Donation(donor_id, donation_date, donation_amount)
            donation3 = Donation(donor_id, donation_date, donation_amount + 0.005)

            self.assertEqual(donation1, donation2)
            self.assertNotEqual(donation1, donation3)