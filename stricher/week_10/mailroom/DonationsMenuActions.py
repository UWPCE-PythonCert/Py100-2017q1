from MenuActions import MenuActions


class DonationsMenuActions(MenuActions):

    from Database import Database
    from sys import stdout
    from Donation import Donation
    from Donor import Donor

    # TODO: complete/update
    # TODO: Add get donations from a donor

    @staticmethod
    def get_list_of_donors(donations_db: Database, ostream=stdout) -> None:
        ostream.write(donations_db.donors_table.get_donors_names())

    @staticmethod
    def record_donation(donations_db: Database, donation: Donation, donor: Donor, ostream=stdout) -> None:
        donations_db.add_donation(donation, donor)

    @staticmethod
    def back_to_home_menu():
        #TODO: implement
        pass