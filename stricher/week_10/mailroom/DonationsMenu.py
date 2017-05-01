
from MultipleChoicesMenu import MultipleChoicesMenu


class DonationsMenu(MultipleChoicesMenu):

    from Database import Database
    from sys import stdin, stdout

    def __init__(self, donations_db: Database, max_menu_calls=100,
                 max_trials=3, istream=stdin, ostream=stdout):

        from DonationsMenuActions import DonationsMenuActions
        self._donations_menu_act = DonationsMenuActions(donations_db, ostream)
        super(DonationsMenu, self).__init__(donations_db, max_menu_calls,
                                            max_trials, istream,
                                            ostream)

    def get_menu_choices_actions(self) -> dict:
        return self._init_menu_choices_actions()

    def _init_menu_choices_actions(self) -> dict:
        # TODO: Add get donations from a donor
        from MenuActions import MenuActions
        return {
            "1": dict(message="Get the list of donors", fun=self._donations_menu_act.get_list_of_donors),
            "2": dict(message="Record a donation", fun=self._donations_menu_act.record_donation),
            "3": dict(message="Get back to the main menu", fun=MenuActions.back_to_home_menu),
            "4": dict(message="quit", fun=MenuActions.go_to_quit_menu)
        }
