from unittest import TestCase


class TestDonorsDBBenchData(TestCase):

    def test_instantiate(self):

        from BenchData import DonorsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date

        donors_db = DonorsDBBenchData().data
        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donor = donors_db[donor_id.value]
        self.assertEqual("M", donor.name.prefix)
        self.assertEqual("Charles", donor.name.first)
        self.assertEqual("Ives", donor.name.last)
        self.assertEqual("14, Avenue Foch", donor.address.street)
        self.assertEqual("75016", donor.address.zipcode)
        self.assertEqual("Paris", donor.address.city)
        self.assertEqual("France", donor.address.country)
        self.assertEqual("+33 1 45 67 83 45", donor.address.phone)
        self.assertEqual("charles.ives@centralparkinthedark.com",
                         donor.address.mail)
        self.assertEqual(date(1874, 10, 20), donor.birth_date)
