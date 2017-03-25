
from UserInputMenu import UserInputMenu


class DonationsMenu(UserInputMenu):

    from Database import Database

    def __init__(self,  donations_db: Database, max_menu_calls=100, max_trials=3):

        from MultipleChoicesMenu import MultipleChoicesMenu

        super(DonationsMenu, self).__init__(donations_db=donations_db,
                                            max_menu_calls=max_menu_calls,
                                            max_trials=max_trials)

        self._menu = MultipleChoicesMenu(menu_choices_actions=self._init_menu_choices_actions(), donations_db=donations_db,
                                         max_menu_calls=max_menu_calls, max_trials=max_trials)

    def _init_menu_choices_actions(self) -> dict:
        from DonationsMenuActions import DonationsMenuActions
        from QuitMenuActions import QuitMenuActions
        donations_menu_act = DonationsMenuActions(self.donations_db)
        quit_menu_act = QuitMenuActions(self.donations_db)
        # TODO: Add get donations from a donor
        return {
            "1": dict(message="Get the list of donors", fun=donations_menu_act.get_list_of_donors),
            "2": dict(message="Record a donation", fun=donations_menu_act.record_donation),
            "3": dict(message="Get back to the main menu", fun=donations_menu_act.back_to_home_menu),
            "4": dict(message="quit", fun=quit_menu_act.quit_program)
        }
