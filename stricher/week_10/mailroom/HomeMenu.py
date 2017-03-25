from MultipleChoicesMenu import MultipleChoicesMenu


class HomeMenu(MultipleChoicesMenu):

    from Database import Database
    from sys import stdin, stdout

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):
        from HomeMenuActions import HomeMenuActions
        from ThankYouEmailMenu import ThankYouEmailMenu
        from QuitMenu import QuitMenu

        self._home_menu_act = HomeMenuActions(donations_db, ostream)
        self._thank_you_email_menu = ThankYouEmailMenu(donations_db,
                                   max_menu_calls,
                                   max_trials,
                                   istream, ostream)
        self._quit_menu = QuitMenu(donations_db,
                                   max_menu_calls,
                                   max_trials,
                                   istream, ostream)
        self._menu_choices_actions = self._init_menu_choices_actions()
        super(HomeMenu, self).__init__(donations_db, max_menu_calls,
                                       max_trials, istream, ostream)

    def get_menu_choices_actions(self) -> dict:
        return self._menu_choices_actions

    def _init_menu_choices_actions(self) -> dict:
        # TODO: add "Access database"
        return {"1": dict(message="Send a thank you email",
                          fun=self._thank_you_email_menu.get_input_from_user),
                "2": dict(message="Create a report",
                          fun=self._home_menu_act.create_report),
                "3": dict(message="quit",
                          fun=self._quit_menu.get_action_from_user_and_perform)}
