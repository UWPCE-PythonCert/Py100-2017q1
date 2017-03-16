
#TODO: complete/update

from MultipleChoicesMenu import MultipleChoicesMenu


class HomeMenu(MultipleChoicesMenu):

    from HomeMenuActions import HomeMenuActions

    __valid_choices = \
        {
            "1": dict(message="Send a Thank you", fun=HomeMenuActions.thank_you),
            "2": dict(message="Create a report", fun=HomeMenuActions.create_report),
            "3": dict(message="quit", fun=HomeMenuActions.quit_program)
        }

    def __init__(self, max_menu_calls=100, max_trials=3):
        super(HomeMenu, self).__init__(max_menu_calls=max_menu_calls,
                                       max_trials=max_trials)

    def _get_valid_choices(self) -> dict:
        return self.__valid_choices

    def _make_request_string(self) -> str:
        request = "\nPlease choose one of the following actions ("
        for index in range(self._get_num_valid_choices()):
            sep = "" if index == 0 else "-"
            request += sep + str(index + 1)
        return request + "):" + 2 * "\n"

    def _make_menu_string(self) -> str:
        menu = ""
        for index in range(self._get_num_valid_choices()):
            menu += "({}) ".format(index + 1) + \
                    self._get_valid_choices()[str(index + 1)]["message"] +\
                    "\n"
        return menu + "\n"

    def _make_invalid_int_error_string(self) -> str:
        return 2 * "\n" + "Invalid input. Please enter a number between {} and {}!\n"\
            .format(1, self._get_num_valid_choices())

