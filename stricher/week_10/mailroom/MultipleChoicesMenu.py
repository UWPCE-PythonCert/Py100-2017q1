from Menu import Menu


class MultipleChoicesMenu(Menu):

    from Database import Database
    from io import IOBase

    def __init__(self, donations_db: Database, max_menu_calls: int,
                 max_trials: int, istream: IOBase, ostream: IOBase):
        super(MultipleChoicesMenu, self).__init__(donations_db=donations_db,
                                                  max_menu_calls=max_menu_calls,
                                                  max_trials=max_trials,
                                                  istream=istream,
                                                  ostream=ostream)
        self._user_choice = ""

    def get_menu_choices_actions(self) -> dict:
        pass

    def _get_num_choices_actions(self) -> int:
        return len(self.get_menu_choices_actions())

    #TODO: change insertion method
    def register_choice(self, message: str, fun) -> None:
        index = str(self._get_num_choices_actions() + 1)
        self.get_menu_choices_actions()[index] = {}
        self.get_menu_choices_actions()[index] = dict(message=message, fun=fun)

    def _is_valid_choice(self, ans: str) -> bool:
        return ans in self.get_menu_choices_actions().keys()

    def _validate_user_choice(self, ans: str) -> str:
        if not self._is_valid_choice(ans):
            from InvalidUserChoice import InvalidUserChoice
            raise InvalidUserChoice(self.messages["error"])
        self._user_choice = ans
        return ans

    def _make_request_string(self, add_message="") -> str:
        request = "\nPlease choose one of the following actions ("
        for index in range(self._get_num_choices_actions()):
            sep = "" if index == 0 else "-"
            request += sep + str(index + 1)
        return request + "){}:".format(add_message) + 2 * "\n"

    def _make_menu_string(self) -> str:
        menu = ""
        for index in range(self._get_num_choices_actions()):
            menu += "({}) ".format(index + 1) + \
                    self.get_menu_choices_actions()[str(index + 1)]["message"] + \
                    "\n"
        return menu + "\n"

    def _make_error_string(self) -> str:
        return "\n" + "Invalid input. Please enter a number between {} and {}!\n" \
            .format(1, self._get_num_choices_actions())

    def _get_action(self, ans):
        return self.get_menu_choices_actions()[self._validate_user_choice(ans)]["fun"]

    def _get_quit_menu(self):
        from QuitMenu import QuitMenu
        quit_menu = QuitMenu(self.donations_db, max_trials=self._max_trials,
                             max_menu_calls=self.max_menu_calls,
                             istream=self.istream, ostream=self.ostream)
        quit_menu.get_action_from_user_and_perform()

    def _get_action_from_user(self):
        from io import StringIO

        def __reset_ostream() -> None:
            self.ostream.truncate(0)
            self.ostream.seek(0)

        def __recurs(counter):
            from InvalidUserChoice import InvalidUserChoice
            from GoToQuitMenu import GoToQuitMenu
            except_str = "From MultipleChoicesMenu"
            ans = self._print_request_and_menu()
            try:
                ans = self._validate_user_choice(ans)
                return self._get_action(ans)
            except InvalidUserChoice as inv_uc:
                if type(self.ostream) == StringIO:
                    __reset_ostream()
                self.ostream.write(str(inv_uc))
            if counter == self.max_trials:
                raise GoToQuitMenu(except_str)
            return __recurs(counter + 1)

        return __recurs(counter=1)

    @staticmethod
    def perform_action_from_user(fun):
        fun()

    def get_action_from_user_and_perform(self):

        def __recurs(counter):
            if counter == self._max_menu_calls:
                self._get_quit_menu()
            action = self._get_action_from_user()
            MultipleChoicesMenu.perform_action_from_user(action)
            return __recurs(counter + 1)

        return __recurs(counter=0)
