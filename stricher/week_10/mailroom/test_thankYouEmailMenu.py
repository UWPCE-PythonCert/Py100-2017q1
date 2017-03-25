from unittest import TestCase


class TestThankYouEmailMenu(TestCase):
    from Database import Database

    @staticmethod
    def __init_db(self) -> Database:

        from Database import Database
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData

        return Database(DonorsTable(DonorsDBBenchData().data),
                        DonationsTable(DonationsDBBenchData().data))

    def test__is_valid_choice(self):
        self.fail()

    def test__validate_user_choice(self):
        self.fail()

    def test__make_request_string(self):
        self.fail()

    def test_get_action_from_user_and_perform(self):
        self.fail()
