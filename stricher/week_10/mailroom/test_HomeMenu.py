from unittest import TestCase


class TestMenu(TestCase):

    @staticmethod
    def _helper_make_db():
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from Database import Database
        return Database(DonorsTable(DonorsDBBenchData().data),
                        DonationsTable(DonationsDBBenchData().data))

    def test__make_request_string(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        menu_test_data = HomeMenuBenchData()
        self.assertEqual(menu._menu._make_request_string(),
                         menu_test_data.get_request_to_user())

    def test__make_menu_string(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        menu_test_data = HomeMenuBenchData()
        self.assertEqual(menu._menu._make_menu_string(),
                         menu_test_data.get_menu())

    def test__make_invalid_choice_error_string(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        menu_test_data = HomeMenuBenchData()
        self.assertEqual(menu._menu._make_error_string(),
                         menu_test_data.get_menu_error_message())

    def test__make_quit_string(self):
        from HomeMenu import HomeMenu
        from BenchData import MenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        menu_test_data = MenuBenchData()
        self.assertEqual(menu._menu._make_quit_string(),
                         menu_test_data.get_quit_message())

    def test__get_request_to_user(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        menu_test_data = HomeMenuBenchData()
        self.assertEqual(menu_test_data.get_request_to_user(),
                         menu.messages["request"])

    def test__get_menu(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        self.assertEqual(HomeMenuBenchData.get_menu(),
                         menu._menu._make_menu_string())

    def test__get_error_message(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from BenchData import DonorsDBBenchData, DonationsDBBenchData
        from Database import Database
        db = Database(DonorsTable(DonorsDBBenchData().data),
                      DonationsTable(DonationsDBBenchData().data))
        menu = HomeMenu(db)
        self.assertEqual(HomeMenuBenchData.get_menu_error_message(),
                         menu.messages["error"])

    def test__get_quit_message(self):
        from HomeMenu import HomeMenu
        from BenchData import HomeMenuBenchData
        menu = HomeMenu(TestMenu._helper_make_db())
        self.assertEqual(HomeMenuBenchData.get_quit_message(),
                         menu._menu.messages["quit"])

    def test__is_valid(self):
        from HomeMenu import HomeMenu
        menu = HomeMenu(TestMenu._helper_make_db())
        self.assert_(menu._menu._is_valid_choice("1"))
        self.assert_(menu._menu._is_valid_choice("2"))
        self.assert_(menu._menu._is_valid_choice("3"))
        self.assert_(not menu._menu._is_valid_choice("4"))
        self.assert_(not menu._menu._is_valid_choice("qwert"))
        self.assert_(not menu._menu._is_valid_choice("0"))

    def test__print_request_and_menu(self):

        def __test_helper(user_input: str) -> None:
            from HomeMenu import HomeMenu
            from io import StringIO
            from BenchData import HomeMenuBenchData
            ostream = StringIO()
            istream = StringIO(user_input)
            menu = HomeMenu(TestMenu._helper_make_db())
            user_ans = menu._menu._print_request_and_menu(ostream, istream)
            bench_str = HomeMenuBenchData.get_request_to_user() \
                        + HomeMenuBenchData.get_menu() \
                        + HomeMenuBenchData.get_input_str()
            self.assertEqual(bench_str, ostream.getvalue())
            self.assertNotEqual(bench_str + "\n", ostream.getvalue())
            self.assertEqual(user_input, user_ans)
            self.assertNotEqual(user_input + "?", user_ans)

        __test_helper("1")
        __test_helper("2")
        __test_helper("qwerty")

    def test__validate_user_choice(self):

        def __test_helper(ans: str) -> None:

            from HomeMenu import HomeMenu
            from io import StringIO
            from InvalidUserChoice import InvalidUserChoice

            ostream = StringIO()
            menu = HomeMenu(TestMenu._helper_make_db())
            try:
                tested_ans = menu._menu._validate_user_choice(ans)
            except InvalidUserChoice as inv_uc:
                self.assertEqual(menu._menu.messages["error"], str(inv_uc))
            else:
                self.assertEqual(ans, tested_ans)
                self.assertNotEqual(ans, tested_ans + "e")

        __test_helper("1")
        __test_helper("2")
        __test_helper("3")
        __test_helper("4")
        __test_helper("")
        __test_helper("0")
        __test_helper("QWERT")

    def test_get_action(self):

        from HomeMenu import HomeMenu
        from HomeMenuActions import HomeMenuActions
        from QuitMenuActions import QuitMenuActions
        from PersonId import PersonId
        from Name import PersonName
        from datetime import date
        from io import StringIO

        donations_db = TestMenu._helper_make_db()
        home_menu_act = HomeMenuActions(donations_db)
        quit_menu_act = QuitMenuActions(donations_db)
        home_menu = HomeMenu(donations_db)

        donations = donations_db.get_donation(PersonId(PersonName("M", "Charles", "Ives"), date(1874, 10, 20)),
                                              date(2014, 2, 8))
        ostream = StringIO()

        self.assertEqual(home_menu_act.send_a_thank_you_email(donations[0], ostream), home_menu._menu._get_action("1")(donations[0], ostream))
        print(ostream.getvalue())
        self.assertEqual(home_menu_act.create_report, home_menu._menu._get_action("2"))
        self.assertEqual(quit_menu_act.quit_program, home_menu._menu._get_action("3"))

    def test_get_action_from_user(self) -> None:

        from io import StringIO

        def __test_helper(user_input: str, bench_str: str, max_trials=3) -> None:

            from HomeMenu import HomeMenu

            ostream = StringIO()
            istream = StringIO(user_input)
            menu = HomeMenu(TestMenu._helper_make_db())
            ans = menu._menu._get_action_from_user(istream, ostream)
            user_input = user_input.split('\n')
            last_user_input = user_input[min(max_trials, len(user_input)) - 1]
            self.assertEqual(ostream.getvalue(), bench_str)
            try:
                self.assertEqual(menu._menu._get_action(last_user_input), ans)
            except ValueError as ve:
                self.assertEqual("HomeMenu._get_action(ans) - "
                                 "Invalid argument ans", str(ve))

        from BenchData import HomeMenuBenchData

        menu_tests_data = HomeMenuBenchData()
        menu_bench_str = menu_tests_data.get_request_to_user() \
                         + menu_tests_data.get_menu() \
                         + menu_tests_data.get_input_str()
        invalid_plus_menu_bench_str = menu_tests_data.get_menu_error_message() \
                                      + menu_tests_data.get_request_to_user() \
                                      + menu_tests_data.get_menu() \
                                      + menu_tests_data.get_input_str()
        menu_quit_str = menu_tests_data.get_quit_message()

        __test_helper("1", menu_bench_str)
        __test_helper("2", menu_bench_str)
        __test_helper("4\n2", invalid_plus_menu_bench_str)
        __test_helper("0\n2", invalid_plus_menu_bench_str)
        __test_helper("erter\n2", invalid_plus_menu_bench_str)
        __test_helper("0\n4\n3", invalid_plus_menu_bench_str)
        __test_helper("0\n4\nTRE\n2", menu_quit_str)
        __test_helper("0\n0\n0\n0\n0", menu_quit_str)

    def test__perform_action_from_user(self) -> None:

        from BenchData import TestThat

        def __test_helper(user_choice, trace_ref) -> None:
            from HomeMenu import HomeMenu
            from io import StringIO
            istream = StringIO(user_choice)
            ostream = StringIO()
            menu = HomeMenu(TestMenu._helper_make_db())
            requested_action = menu._menu._get_action_from_user(istream, ostream)
            ostream = StringIO()
            menu._menu._perform_action_from_user(fun=requested_action, ostream=ostream)
            test = TestThat()
            print("ostream value: {}".format(ostream.getvalue()))
            self.assertEqual(test.get_trace(trace_ref), ostream.getvalue())

        test_that = TestThat()
        if test_that.do():
            __test_helper("1", "send_a_thank_you_email")
            __test_helper("2", "create_report")
            __test_helper("3", "quit_program")

            __test_helper("4\n2", "create_report")
            __test_helper("0\n2", "create_report")
            __test_helper("erter\n2", "create_report")
            __test_helper("0\n4\n3", "quit_program")
            __test_helper("0\n4\nTRE\n2", "quit_program")
            __test_helper("0\n0\n0\n0\n0", "quit_program")

        else:
            pass

        def test_get_action_from_user_and_perform(self) -> None:
            pass
