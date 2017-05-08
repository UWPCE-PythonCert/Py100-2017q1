from unittest import TestCase


class TestDatabase(TestCase):
    def test___init__(self):
        from Database import Database
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate
        from Donation import Donation

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        donors_bench_data = DonorsDBBenchData().data
        self.assertEqual(db.donors_table._get_person_id(),
                         tuple(donors_bench_data.keys()))

        donor_id = PersonId()
        donation = Donation(donor_id, MyDate(2016, 1, 7), 8000)
        donations_radigue = db.donations_table.get_per_donor(donor_id.value)
        self.assertEqual(dict, type(donations_radigue))
        self.assertEqual(list, type(donations_radigue[MyDate(2016, 1, 7)]))
        self.assertEqual(donation, donations_radigue[MyDate(2016, 1, 7)][0])

    def test_add_donation(self):
        from Database import Database
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate
        from Donation import Donation

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        donor_id = PersonId()
        donations = db.donations_table.get_per_donor_per_date(donor_id.value, MyDate(2012, 4, 12))
        self.assertEqual(2, len(donations))
        donation = Donation(donor_id, MyDate(2012, 4, 12), 567585)
        db.donations_table._add_donation_existing_date(donation)
        donations = db.donations_table.get_per_donor_per_date(donor_id.value, MyDate(2012, 4, 12))
        self.assertEqual(3, len(donations))
        self.assertIn(donation, donations)

    def test_get_donation(self):
        from Database import Database
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        donations_ives = db.get_donation(donor_id=PersonId(),
                                         donation_date=MyDate(2012, 4, 12))
        self.assertEqual(list, type(donations_ives))
        self.assertEqual(567, donations_ives[0].amount)
        self.assertEqual(1000, donations_ives[1].amount)

    def test_get_total_donations_amounts(self):
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        tot_don_amounts = db.donations_table.get_total_donations_amounts()
        donor_id = PersonId()
        self.assertEqual(3567 + 7167, tot_don_amounts[donor_id.value])

    def test_get_average_gift_per_donor(self):
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate

        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))

        avge_gift_donor = db.donations_table.get_average_gift()

        donor_id_charles = PersonId()
        donor_id_jsb = PersonId()
        donor_id_miles = PersonId()

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
