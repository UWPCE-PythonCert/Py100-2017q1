from MenuActions import MenuActions


class DonationsMenuActions(MenuActions):
    from Database import Database
    from sys import stdout
    from Donation import Donation
    from Donor import Donor
    from io import IOBase

    # TODO: complete/update
    # TODO: Add get donations from a donor

    def __init__(self, donations_db, ostream: IOBase):
        super(DonationsMenuActions, self).__init__(donations_db, ostream)

    def get_list_of_donors(self) -> None:
        donors_names = self.donations_db.donors_table.get_persons_names()
        self._ostream.write("\n")
        for name in donors_names:
            self._ostream.write(str(name) + "\n")

    # TODO: Call RecordDonationMenu

    def record_donation(self, donations_db: Database,
                        donation: Donation, donor: Donor,
                        ostream=stdout) -> None:
        # self.db.add_donation(donation, donor)
        pass


    @staticmethod
    def back_to_home_menu():
        # TODO: implement
        pass
