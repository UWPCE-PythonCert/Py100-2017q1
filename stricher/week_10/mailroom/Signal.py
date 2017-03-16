
class Signal:

    __register = dict(quit_program="QUIT_PROGRAM",
                      back_to_home_menu="BACK_TO_HOME_MENU")

    def get_quit_program(self):
        return self.__register["quit_program"]

    def get_back_to_home_menu(self):
        return self.__register["back_to_home_menu"]
