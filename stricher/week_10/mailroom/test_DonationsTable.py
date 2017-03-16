from unittest import TestCase


class TestDonationsTable(TestCase):

    def test_get_donations_per_donor(self):

        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("Ms", "Eliane", "Radigue"), date(1932, 1, 24))
        donation = Donation(donor_id, date(2016, 1, 7), 8000)
        donations_radigue = donations_table.get_per_donor(donor_id.value)
        self.assertEqual(dict, type(donations_radigue))
        self.assertEqual(list, type(donations_radigue[date(2016, 1, 7)]))
        self.assertEqual(donation, donations_radigue[date(2016, 1, 7)][0])

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation_1 = Donation(donor_id, date(2012, 4, 12), 567)
        donation_2 = Donation(donor_id, date(2012, 4, 12), 1000)
        donation_3 = Donation(donor_id, date(2014, 2, 8), 7654)
        donations_ives = donations_table.get_per_donor(donor_id.value)
        self.assertEqual(dict, type(donations_ives))
        self.assertEqual(list, type(donations_ives[date(2012, 4, 12)]))
        self.assertEqual(donation_1, donations_ives[date(2012, 4, 12)][0])
        self.assertEqual(donation_2, donations_ives[date(2012, 4, 12)][1])
        self.assertEqual(donation_3, donations_ives[date(2014, 2, 8)][0])

    def test__get_dates_per_donor(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Wynton", "Kelly"), date(1931, 12, 2))
        donations_dates = donations_table._get_dates_per_donor(donor_id.value)
        self.assertEqual(date(2007, 6, 18), donations_dates[0])

    def test__get_per_donor_per_date(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation_1 = Donation(donor_id, date(2012, 4, 12), 567)
        donation_2 = Donation(donor_id, date(2012, 4, 12), 1000)
        donation_3 = Donation(donor_id, date(2014, 2, 8), 7654)

        donations_date_1 = donations_table._get_per_donor_per_date(donor_id.value, date(2012, 4, 12))
        self.assertEqual(donation_1, donations_date_1[0])
        self.assertEqual(donation_2, donations_date_1[1])
        self.assertEqual(2, len(donations_date_1))
        donations_date_2 = donations_table._get_per_donor_per_date(donor_id.value, date(2014, 2, 8))
        self.assertEqual(donation_3, donations_date_2[0])

    def test__add_date(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)
        donor_id = DonorId(Name("M", "Miles", "Davis"), date(1926, 5, 26))
        donation = Donation(donor_id, date(2008, 1, 23), 5678.56)
        donations_table._add_date(donation)
        donations_dates = donations_table._get_dates_per_donor(donor_id.value)
        self.assertEqual(donation.date, donations_dates[0])

    def test__exists_previous_from_donor_same_date(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation_1 = Donation(donor_id, date(2012, 4, 12), 567)
        donation_2 = Donation(donor_id, date(2012, 4, 12), 1000)
        donation_3 = Donation(donor_id, date(2014, 2, 8), 7654)

        self.assertEqual(True, donations_table.exists_previous_from_donor_same_date(donation_1))
        self.assertEqual(True, donations_table.exists_previous_from_donor_same_date(donation_2))
        self.assertEqual(True, donations_table.exists_previous_from_donor_same_date(donation_3))

    def test__add_donation_existing_date(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation = Donation(donor_id, date(2012, 4, 12), 567585)
        donations_table._add_donation_existing_date(donation)
        donations = donations_table._get_per_donor_per_date(donor_id.value, date(2012, 4, 12))
        self.assertEqual(3, len(donations))
        self.assertIn(donation, donations)

    def test__add_donation_new_date(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        donations_table = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation = Donation(donor_id, date(2000, 6, 12), 4565)
        donations_table._add_donation_new_date(donation)
        donations = donations_table._get_per_donor_per_date(donor_id.value, date(2000, 6, 12))
        self.assertEqual(1, len(donations))
        self.assertIn(donation, donations)

    def test__add_donor(self):
        from DonationsTable import DonationsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date

        db = DonationsTable(DonationsDBBenchData().data)

        donor_id = DonorId(Name("M", "Bill", "Watrous"), date(1954, 5, 13))
        self.assertEqual(False, db._donor_exists_in_database(donor_id.value))
        db._add_donor(donor_id.value)
        self.assertEqual(True, db._donor_exists_in_database(donor_id.value))
