from MultipleChoicesMenu import MultipleChoicesMenu


class HomeMenu(MultipleChoicesMenu):
    from Database import Database
    from sys import stdin, stdout

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):

        from HomeMenuActions import HomeMenuActions
        from DonationsMenu import DonationsMenu
        from ThankYouEmailMenu import ThankYouEmailMenu
        from QuitMenu import QuitMenu

        self._home_menu_act = HomeMenuActions(donations_db, ostream)
        self._donations_menu = DonationsMenu(donations_db,
                                             max_menu_calls,
                                             max_trials,
                                             istream, ostream)
        self._thank_you_email_menu = ThankYouEmailMenu(donations_db,
                                                       max_menu_calls,
                                                       max_trials,
                                                       istream, ostream)
        self.quit_menu = QuitMenu(donations_db,
                                  max_menu_calls,
                                  max_trials,
                                  istream, ostream)
        self._menu_choices_actions = self._init_menu_choices_actions()
        super(HomeMenu, self).__init__(donations_db, max_menu_calls,
                                       max_trials, istream, ostream)

    def get_menu_choices_actions(self) -> dict:
        return self._menu_choices_actions

    def get_action_from_user_and_perform(self):

        def __recurs(counter, go_to_quit_menu=False):

            from GoToQuitMenu import GoToQuitMenu
            from GoBackToHomeMenu import GoBackToHomeMenu

            try:
                if counter == self._max_menu_calls or go_to_quit_menu:
                    self._get_quit_menu()
                else:
                    action = self._get_action_from_user()
                    MultipleChoicesMenu.perform_action_from_user(action)
                    go_to_quit_menu = False
            except GoToQuitMenu:
                go_to_quit_menu = True
                pass
            except GoBackToHomeMenu:
                go_to_quit_menu = False
                pass
            return __recurs(counter + 1, go_to_quit_menu)

        return __recurs(counter=0)

    def _init_menu_choices_actions(self) -> dict:
        # TODO: add "Access database"
        return {"1": dict(message="Display the donations menu",
                          fun=self._donations_menu.get_action_from_user_and_perform),
                "2": dict(message="Send a thank you email",
                          fun=self._thank_you_email_menu.get_input_from_user),
                "3": dict(message="Create a report",
                          fun=self._home_menu_act.create_report),
                "4": dict(message="quit",
                          fun=self.quit_menu.get_action_from_user_and_perform)}
