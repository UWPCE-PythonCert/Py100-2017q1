from unittest import TestCase


class TestDonationsDBBenchData(TestCase):

    def test_instantiate(self):
        from BenchData import DonationsDBBenchData
        from PersonId import PersonId
        from Name import PersonName
        from datetime import date
        from Donation import Donation

        donations_db = DonationsDBBenchData().data
        self.assertEqual(6, len(donations_db))

        # ---- Charles Ives ----
        donor_id = PersonId(PersonName("M", "Charles", "Ives"), date(1874, 10, 20))
        donations = donations_db[donor_id.value]
        self.assertEqual(2, len(donations))
        self.assert_(date(2012, 4, 12) in tuple(donations.keys()))
        self.assert_(date(2014, 2, 8) in tuple(donations.keys()))

        # date 1
        donations_date_1 = donations[date(2012, 4, 12)]
        self.assertEqual(2, len(donations_date_1))
        self.assertEqual(Donation(donor_id, date(2012, 4, 12), 567), donations_date_1[0])
        self.assertEqual(Donation(donor_id, date(2012, 4, 12), 1000), donations_date_1[1])

        # date 2
        donations_date_2 = donations[date(2014, 2, 8)]
        self.assertEqual(1, len(donations_date_2))
        self.assertEqual(Donation(donor_id, date(2014, 2, 8), 7654), donations_date_2[0])

        # ---- Jean S Bach ----
        donor_id = PersonId(PersonName("M", "Jean S", "Bach"), date(1685, 3, 31))
        donations = donations_db[donor_id.value]
        self.assertEqual(3, len(donations))

        donation_dates = [date(2014, 8, 6), date(2011, 12, 25), date(2016, 4, 1)]
        amounts = [2897, 4567, 876]

        for don_date, don_amount in zip(donation_dates, amounts):
            dons = donations[don_date]
            self.assertEqual(1, len(dons))
            self.assertEqual(Donation(donor_id, don_date, don_amount), donations[don_date][0])

        # ---- Lee Morgan ----
        donor_id = PersonId(PersonName("M", "Lee", "Morgan"), date(1938, 7, 10))
        donations = donations_db[donor_id.value]
        self.assertEqual(2, len(donations))

        donation_dates = [date(2015, 10, 23), date(2016, 10, 14)]
        amounts = [3567, 7167]

        for don_date, don_amount in zip(donation_dates, amounts):
            dons = donations[don_date]
            self.assertEqual(1, len(dons))
            self.assertEqual(Donation(donor_id, don_date, don_amount), donations[don_date][0])

        # ---- Miles Davis ----
        donor_id = PersonId(PersonName("M", "Miles", "Davis"), date(1926, 5, 26))
        donations = donations_db[donor_id.value]
        self.assertEqual(1, len(donations))

        donation_dates = [date(2011, 5, 19)]
        amounts = [67000, 15000]

        index = 0
        for don_amount in amounts:
            dons = donations[donation_dates[0]]
            self.assertEqual(2, len(dons))
            self.assertEqual(Donation(donor_id, donation_dates[0], don_amount), donations[donation_dates[0]][index])
            index += 1

        # ---- Wynton Kelly ----
        donor_id = PersonId(PersonName("M", "Wynton", "Kelly"), date(1931, 12, 2))
        donations = donations_db[donor_id.value]
        self.assertEqual(3, len(donations))

        donation_dates = [date(2009, 2, 24), date(2007, 6, 18), date(2013, 4, 5)]
        amounts = [7894, 6666, 657]

        for don_date, don_amount in zip(donation_dates, amounts):
            dons = donations[don_date]
            self.assertEqual(1, len(dons))
            self.assertEqual(Donation(donor_id, don_date, don_amount), donations[don_date][0])

        # ---- Eliane Radigue ----
        donor_id = PersonId(PersonName("Ms", "Eliane", "Radigue"), date(1932, 1, 24))
        donations = donations_db[donor_id.value]
        self.assertEqual(1, len(donations))

        donation_dates = [date(2016, 1, 7)]
        amounts = [8000]

        dons = donations[donation_dates[0]]
        self.assertEqual(1, len(dons))
        self.assertEqual(Donation(donor_id, donation_dates[0], amounts[0]), donations[donation_dates[0]][0])
