
#TODO: complete/update

class Menu:

    from io import IOBase

    def __init__(self, max_menu_calls=100, max_trials=3):
            self.__max_menu_calls = max_menu_calls
            self.__max_trials = max_trials
            self.__messages = dict()
            self.__messages["request"] = self._make_request_string()
            self.__messages["menu"] = self._make_menu_string()
            self.__messages["input"] = self._make_input_str()
            self.__messages["error"] = self._make_invalid_int_error_string()
            self.__messages["quit"] = self._make_quit_string()

    def _get_valid_choices(self) -> dict:
        pass

    def _make_request_string(self) -> str:
        pass

    def _make_menu_string(self) -> str:
        pass

    def _make_input_str(self) -> str:
        return "Enter: "

    def _make_invalid_int_error_string(self) -> str:
        pass

    def _make_quit_string(self) -> str:
        return "\n\nInvalid entry. Maximum number of allowed" \
               " trials reached ({}).\n"\
            .format(self.__max_trials)

    def _get_num_valid_choices(self) -> int:
        return len(self._get_valid_choices())

    def register_choice(self, message: str, fun) -> None:
        index = str(self._get_num_valid_choices() + 1)
        self._get_valid_choices()[index] = {}
        self._get_valid_choices()[index] = dict(message=message, fun=fun)

    def _get_request_to_user(self) -> str:
        return self.__messages["request"]

    def _get_menu(self) -> str:
        return self.__messages["menu"]

    def _get_input_str(self) -> str:
        return self.__messages["input"]

    def _get_error_message(self) -> str:
        return self.__messages["error"]

    def _get_quit_message(self) -> str:
        return self.__messages["quit"]

    def _print_request_and_menu(self, ostream: IOBase, istream: IOBase) -> str:
        from Utilities import Utilities
        return Utilities.request(ostream, istream,
                                 self._get_request_to_user() +
                                 self._get_menu() +
                                 self._get_input_str())

    def _is_valid(self, ans: str) -> bool:
        return ans in self._get_valid_choices().keys()

    def _validate_user_choice(self, ans: str) -> str:
        if not self._is_valid(ans):
            from InvalidUserChoice import InvalidUserChoice
            raise InvalidUserChoice(self._get_error_message())
        return ans

    def _get_action(self, ans):
        if self._is_valid(ans):
            return self._get_valid_choices()[ans]["fun"]
        else:
            raise ValueError("HomeMenu._get_action(ans) -"
                             " Invalid argument ans")

    def _get_action_from_user(self, istream: IOBase,
                              ostream: IOBase):
        from io import StringIO

        def __reset_ostream() -> None:
            ostream.truncate(0)
            ostream.seek(0)

        def __recurs(counter):
            ans = self._print_request_and_menu(ostream, istream)
            from InvalidUserChoice import InvalidUserChoice
            try:
                ans = self._validate_user_choice(ans)
                return self._get_action(ans)
            except InvalidUserChoice:
                if type(ostream) == StringIO:
                    __reset_ostream()
                if counter == self.__max_trials:
                    from MenuActions import MenuActions
                    ostream.write(self._get_quit_message())
                    return MenuActions.quit_program
                ostream.write(self._get_error_message())
                return __recurs(counter+1)

        return __recurs(counter=1)

    #TODO: allow for arbitrary arguments (*args or *kwargs)
    def _perform_action_from_user(self, fun, ostream):
        return fun(ostream)

    def get_action_from_user_and_perform(self, istream: IOBase, ostream: IOBase):

        from MenuActions import MenuActions
        from Signal import Signal
        signal = Signal()

        def __recurs(counter):
            if counter == self.__max_menu_calls:
                return MenuActions.quit_program(ostream=ostream)
            action = self._get_action_from_user(istream, ostream)
            sig = self._perform_action_from_user(action, ostream)
            if sig == signal.get_quit_program():
                return signal.get_quit_program()
            return __recurs(counter + 1)

        return __recurs(counter=0)



