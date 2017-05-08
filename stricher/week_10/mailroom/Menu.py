# TODO: complete/update

from enum import Enum


class WhichLimit(Enum):
    trials = "max_trials"
    menu_calls = "max_menu_calls"


class Menu:
    from Database import Database

    def __init__(self, donations_db: Database, max_menu_calls, max_trials, istream, ostream):
        self._donations_db = donations_db
        self._max_menu_calls = max_menu_calls
        self._max_trials = max_trials
        self.istream = istream
        self.ostream = ostream
        self._messages = dict()
        self._messages["request"] = self._make_request_string()
        self._messages["menu"] = self._make_menu_string()
        self._messages["input"] = self._make_input_string()
        self._messages["error"] = self._make_error_string()
        self._messages["quit_user"] = self._make_quit_string_from_user()
        self._messages["quit_max_trials"] = self._make_quit_string_limit_exceeded("trials")
        self._messages["quit_max_menu_calls"] = self._make_quit_string_limit_exceeded("menu calls")

    @property
    def donations_db(self):
        return self._donations_db

    @property
    def max_menu_calls(self) -> int:
        return self._max_menu_calls

    @property
    def max_trials(self) -> int:
        return self._max_trials

    @property
    def messages(self) -> dict:
        return self._messages

    def _make_request_string(self) -> str:
        pass

    def _make_menu_string(self) -> str:
        pass

    @staticmethod
    def _make_input_string() -> str:
        return "Enter: "

    def _make_error_string(self) -> str:
        return "\n\nInvalid input\n"

    @staticmethod
    def _make_quit_string_from_user() -> str:
        return "\n\nThe program quits. Goodbye!\n"

    def _make_quit_string_limit_exceeded(self, which_limit: str) -> str:
        store_limits = {"trials": self.max_trials, "menu calls": self.max_menu_calls}
        return "Maximum number of allowed {} reached ({})." \
               " The program is about to quit.\n"\
            .format(which_limit, store_limits[which_limit])

    def _print_request_and_menu(self) -> str:
        from Utilities import Utilities
        return Utilities.request(self.ostream,
                                 self.istream,
                                 self.messages["request"] +
                                 self.messages["menu"] +
                                 self.messages["input"])
