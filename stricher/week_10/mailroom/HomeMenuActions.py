
#TODO: complete/update

from MenuActions import MenuActions


class HomeMenuActions(MenuActions):

    from io import IOBase
    from Database import Database

    def __init__(self, donations_db: Database, ostream: IOBase):
        super(HomeMenuActions, self).__init__(donations_db, ostream)

    def create_report(self):
        from BenchData import TestThat
        test_that = TestThat()
        if test_that.do():
            self._ostream.write(test_that.get_trace("create_report"))
        else:
            from ReportGenerator import ReportDonationsDBGenerator
            report_gen = ReportDonationsDBGenerator(self.donations_db)
            report_gen.write(self._ostream)
