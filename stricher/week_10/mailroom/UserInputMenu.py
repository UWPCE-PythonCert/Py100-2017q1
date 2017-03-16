
from Menu import Menu


class UserInputMenu(Menu):
    def __init__(self, max_menu_calls, max_trials):
        super(UserInputMenu, self).__init__(max_menu_calls=max_menu_calls,
                                            max_trials=max_trials)
