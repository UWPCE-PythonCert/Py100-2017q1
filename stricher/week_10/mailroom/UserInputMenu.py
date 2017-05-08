
from Menu import Menu


class UserInputMenu(Menu):

    from Database import Database
    from io import IOBase

    def __init__(self, donations_db: Database,
                 max_menu_calls: int, max_trials: int,
                 istream: IOBase, ostream: IOBase):
        self._index = 0
        self._num_calls = 0
        self._trials_counter = 0
        super(UserInputMenu, self).__init__(donations_db=donations_db,
                                            max_menu_calls=max_menu_calls,
                                            max_trials=max_trials,
                                            istream=istream,
                                            ostream=ostream)

    def _make_request_string(self) -> str:
        from Signals import Signals
        return "({} to get back to the home menu - {} to quit)".\
            format(Signals.HOME_MENU.value, Signals.QUIT.value)

    def _make_menu_string(self) -> str:
        pass

    @staticmethod
    def _switch_menu_or_process(input: str, message: str) -> str:
        from Signals import Signals
        input_upper = input.upper()
        if input_upper == Signals.HOME_MENU.value:
            from GoBackToHomeMenu import GoBackToHomeMenu
            raise GoBackToHomeMenu(message)
        if input_upper == Signals.QUIT.value:
            from GoToQuitMenu import GoToQuitMenu
            raise GoToQuitMenu(message)
        return input

    def _is_valid_input(self, input: str) -> bool:
        pass

    def _validate_user_input(self, input: str) -> None:
        from InvalidInput import InvalidInput
        if not self._is_valid_input(input):
            raise InvalidInput("InvalidInput - "
                               "UserInputMenu._validate_user_input(input)")

    def _do_continue(self):
        pass

    def _process(self):
        pass

    def _record_input(self, user_input: str):
        pass

    def _increment_counter(self):
        self._index += 1
        self._num_calls += 1

    def _reset_counter(self):
        self._index = 0
        self._num_calls = 0

    def get_input_from_user(self):
        from io import StringIO

        def __reset_ostream() -> None:
            self.ostream.truncate(0)
            self.ostream.seek(0)

        def __recurs(counter):
            from InvalidInput import InvalidInput
            ans = self._print_request_and_menu()
            try:
                ans = self._switch_menu_or_process(ans, "From UserInputMenu")
                self._validate_user_input(ans)
                self._record_input(ans)
                if not self._do_continue():
                    self._process()
                    return
            except InvalidInput:
                self._trials_counter += 1
                if type(self.ostream) == StringIO:
                    __reset_ostream()
                if self._trials_counter == self.max_trials:
                    from QuitMenu import QuitMenu
                    quit_menu = QuitMenu(self.donations_db,
                                         max_trials=self._max_menu_calls)
                    quit_menu.get_action_from_user_and_perform()
            else:
                self._increment_counter()
                self._trials_counter = 0
            return __recurs(counter + 1)

        return __recurs(counter=0)
