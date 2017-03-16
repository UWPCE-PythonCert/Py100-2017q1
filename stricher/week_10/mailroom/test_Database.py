from unittest import TestCase


class TestDatabase(TestCase):
    def test___init__(self):
        from Database import Database
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        donors_bench_data = DonorsDBBenchData().data
        self.assertEqual(db.donors_table._get_donors_id(),
                         tuple(donors_bench_data.keys()))

        donor_id = DonorId(Name("Ms", "Eliane", "Radigue"), date(1932, 1, 24))
        donation = Donation(donor_id, date(2016, 1, 7), 8000)
        donations_radigue = db.donations_table.get_per_donor(donor_id.value)
        self.assertEqual(dict, type(donations_radigue))
        self.assertEqual(list, type(donations_radigue[date(2016, 1, 7)]))
        self.assertEqual(donation, donations_radigue[date(2016, 1, 7)][0])

    def test_add_donation(self):
        from Database import Database
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        from Donation import Donation

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation = Donation(donor_id, date(2012, 4, 12), 567585)
        db.donations_table._add_donation_existing_date(donation)
        donations = db.donations_table._get_per_donor_per_date(donor_id.value, date(2012, 4, 12))
        self.assertEqual(3, len(donations))
        self.assertIn(donation, donations)

    def test_get_total_donations_amounts(self):
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        tot_don_amounts = db.donations_table.get_total_donations_amounts()
        donor_id = DonorId(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        self.assertEqual(3567 + 7167, tot_don_amounts[donor_id.value])

    def test_get_average_gift_per_donor(self):
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData
        from DonorId import DonorId
        from Name import Name
        from datetime import date

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        avge_gift_donor = db.donations_table.get_average_gift()

        donor_id_charles = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donor_id_jsb = DonorId(Name("M", "Jean S", "Bach"), date(1685, 3, 31))
        donor_id_miles = DonorId(Name("M", "Miles", "Davis"), date(1926, 5, 26))

        self.assertEqual((567 + 1000 + 7654) / 3, avge_gift_donor[donor_id_charles.value])
        self.assertEqual((2897 + 4567 + 876) / 3, avge_gift_donor[donor_id_jsb.value])
        self.assertEqual((67000 + 15000) / 2, avge_gift_donor[donor_id_miles.value])

    def test_get_donors_names_sorted_per_total_hist_donation_amount(self):
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        donors_names = db.get_donors_names_sorted_per_total_hist_donation_amount()
        self.assertEqual("Ms Eliane Radigue", str(donors_names[0]))
        self.assertEqual("M Jean S Bach", str(donors_names[1]))