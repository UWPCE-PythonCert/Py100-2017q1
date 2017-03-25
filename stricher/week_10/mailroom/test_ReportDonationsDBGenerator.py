from unittest import TestCase


class TestData:

    @staticmethod
    def bench_str() -> str:
        return \
            '\nList of donors:\n\n' \
            '***************************************************************************************************\n' \
            '        PersonName        |         Total amount         |   Number of donations   |  Average donation  |\n' \
            '***************************************************************************************************\n' \
            'Ms Eliane Radigue   |                       8000.00|                        1|             8000.00|\n' \
            'M Jean S Bach       |                       8340.00|                        3|             2780.00|\n' \
            'M Charles Ives      |                       9221.00|                        3|             3073.67|\n' \
            'M Lee Morgan        |                      10734.00|                        2|             5367.00|\n' \
            'M Wynton Kelly      |                      15217.00|                        3|             5072.33|\n' \
            'M Miles Davis       |                      82000.00|                        2|            41000.00|\n' \
            '***************************************************************************************************\n'


class TestReportDonationsDBGenerator(TestCase):

    from Database import Database

    @staticmethod
    def _init_db() -> Database:
        from Database import Database
        from BenchData import DonorsDBBenchData
        from DonationsTable import DonationsTable
        from DonorsTable import DonorsTable
        from BenchData import DonationsDBBenchData

        return Database(DonorsTable(DonorsDBBenchData().data),
                        DonationsTable(DonationsDBBenchData().data))

    def test_write(self):

        self.maxDiff = None

        from ReportGenerator import ReportDonationsDBGenerator
        from io import StringIO

        db = self._init_db()
        report_gen = ReportDonationsDBGenerator(db)

        ostream = StringIO()
        report_gen.write(ostream)

        self.assertEqual(TestData.bench_str(), ostream.getvalue())

    def test___str___(self):
        from ReportGenerator import ReportDonationsDBGenerator

        db = self._init_db()
        self.assertEqual(TestData.bench_str(), str(ReportDonationsDBGenerator(db)))
