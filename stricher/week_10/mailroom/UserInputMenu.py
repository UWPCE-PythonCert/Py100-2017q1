
from Menu import Menu


class UserInputMenu(Menu):

    from Database import Database
    from io import IOBase

    def __init__(self, donations_db: Database, max_menu_calls: int, max_trials: int,
                 istream: IOBase, ostream: IOBase):
        super(UserInputMenu, self).__init__(donations_db=donations_db,
                                            max_menu_calls=max_menu_calls,
                                            max_trials=max_trials,
                                            istream=istream,
                                            ostream=ostream)

    def _make_menu_string(self) -> str:
        pass

    def _is_valid_input(self, input: str) -> bool:
        pass

    def _validate_user_input(self, input: str):
        if self._is_valid_input(input):
            return input
        from InvalidInput import InvalidInput
        raise InvalidInput("Invalid input")

    def _do_continue(self):
        pass

    def _record_input(self, input: str):
        pass

    def get_input_from_user(self):
        from io import StringIO

        def __reset_ostream() -> None:
            self.ostream.truncate(0)
            self.ostream.seek(0)

        def __recurs(counter):
            from InvalidInput import InvalidInput
            ans = self._print_request_and_menu()
            try:
                ans = self._validate_user_input(ans)
                if not self._do_continue():
                    return
            except InvalidInput:
                if type(self.ostream) == StringIO:
                    __reset_ostream()
                if counter == self.max_trials:
                    from QuitMenu import QuitMenu
                    quit_menu = QuitMenu(self.donations_db, max_trials=self._max_menu_calls)
                    quit_menu.get_action_from_user_and_perform()
            return __recurs(counter + 1)

        return __recurs(counter=0)
