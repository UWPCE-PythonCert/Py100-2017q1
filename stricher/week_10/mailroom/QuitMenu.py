from MultipleChoicesMenu import MultipleChoicesMenu


class QuitMenu(MultipleChoicesMenu):

    from Database import Database
    from sys import stdin, stdout

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):

        from QuitMenuActions import QuitMenuActions

        self._quit_menu_act = QuitMenuActions(donations_db, ostream)
        self._menu_choices_actions = self._init_menu_choices_actions()
        super(QuitMenu, self).__init__(donations_db, max_menu_calls,
                                        max_trials, istream, ostream)

    def get_menu_choices_actions(self) -> dict:
        return self._menu_choices_actions

    def _init_menu_choices_actions(self) -> dict:
        return {
            "1": dict(message="Save the database to a SQLite database",
                      fun=self._quit_menu_act.save_database_sql_lite),
            "2": dict(message="Save the database to a SQL server database",
                      fun=self._quit_menu_act.save_database_sql_server),
            "3": dict(message="Exit without saving the database",
                      fun=self._quit_menu_act.quit_program)
        }
