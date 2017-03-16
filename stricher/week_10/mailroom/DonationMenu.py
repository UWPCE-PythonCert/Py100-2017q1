
from MultipleChoicesMenu import MultipleChoicesMenu
from UserInputMenu import UserInputMenu

class DonationMenu(MultipleChoicesMenu, UserInputMenu):

    from HomeMenuActions import HomeMenuActions
    from DonationsMenuActions import DonationsMenuActions

    __valid_choices = \
        {
            "1": dict(message="Get the list of donors", fun=DonationsMenuActions.get_list_of_donors),
            "2": dict(message="Record a donation", fun=DonationsMenuActions.record_donation),
            "3": dict(message="Get back to the main menu", fun=DonationsMenuActions.back_to_home_menu),
            "4": dict(message="quit", fun=HomeMenuActions.quit_program)
        }

    def __init__(self, max_menu_calls=100, max_trials=3):
        super(UserInputMenu, self).__init__(max_menu_calls=max_menu_calls,
                                            max_trials=max_trials)
