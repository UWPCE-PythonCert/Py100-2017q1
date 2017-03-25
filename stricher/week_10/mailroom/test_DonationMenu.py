
#TODO: complete/update

from unittest import TestCase


class TestDonationMenu(TestCase):

    def test__init(self):

        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from DonationsMenu import DonationsMenu
        from Database import Database
        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        menu = DonationsMenu(db)
