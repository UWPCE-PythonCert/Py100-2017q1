from unittest import TestCase


class TestDonationsDBBenchData(TestCase):

    def test_instantiate(self):

        from BenchData import DonationsDBBenchData
        from MyDate import MyDate

        donations_db = DonationsDBBenchData().data
        self.assertEqual(6, len(donations_db))

        def __test_equal_donations(email: str, dates: list, amounts: list):
            from BenchData import DonationsDBBenchData

            donations_bench = DonationsDBBenchData()
            donations_raw_data = donations_bench.get_donations_list_from_raw_data(email=email,
                                                                                  donation_dates=dates,
                                                                                  donation_amounts=amounts)
            donations_from_bench_db = donations_bench.get_donations_list_from_bench_db(email=email)
            self.assertListEqual(donations_raw_data, donations_from_bench_db)

        # ---- Charles Ives ----
        email = "charles.ives@centralparkinthedark.com"
        donation_dates = [MyDate(2012, 4, 12), MyDate(2014, 2, 8)]
        amounts = [[567, 1000], 7654]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)

        # ---- Jean S Bach ----
        email = "js.bach@google.com"
        donation_dates = [MyDate(2014, 8, 6), MyDate(2011, 12, 25), MyDate(2016, 4, 1)]
        amounts = [2897, 4567, 876]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)

        # ---- Lee Morgan ----
        email = "lee.morgan@jazzmessengers.com"
        donation_dates = [MyDate(2015, 10, 23), MyDate(2016, 10, 14)]
        amounts = [3567, 7167]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)

        # ---- Miles Davis ----
        email = "miles.davis@myself.com"
        donation_dates = [MyDate(2011, 5, 19)]
        amounts = [[67000, 15000]]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)

        # ---- Wynton Kelly ----
        email = "wynton.kelly@quintet.com"
        donation_dates = [MyDate(2009, 2, 24), MyDate(2007, 6, 18), MyDate(2013, 4, 5)]
        amounts = [7894, 6666, 657]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)

        # ---- Eliane Radigue ----
        email = "eliane.radigue@ircam.com"
        donation_dates = [MyDate(2016, 1, 7)]
        amounts = [8000]
        __test_equal_donations(email=email,
                               dates=donation_dates,
                               amounts=amounts)
