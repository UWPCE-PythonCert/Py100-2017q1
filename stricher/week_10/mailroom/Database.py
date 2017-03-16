
class Database:

    from Donation import Donation
    from Donor import Donor
    from DonorsTable import DonorsTable
    from DonationsTable import DonationsTable

    def __init__(self, donors_table=None, donations_table=None):

        if donors_table is None and donations_table is None:
            self.__donors_table = dict()
            self.__donations_table = dict()
        if donors_table is None or donations_table is None:
            raise ValueError(
                "ValueError - Database(donors_table, donations_table): missing argument"
            )
        self.__donors_table = donors_table
        self.__donations_table = donations_table

    @property
    def donors_table(self) -> DonorsTable:
        return self.__donors_table

    @property
    def donations_table(self) -> DonationsTable:
        return self.__donations_table

    def add_donation(self, donation: Donation, donor: Donor) -> None:
        if donation.donor_id != donor.id:
            raise ValueError("ValueError - Database.add_donation(donation, donor): "
                             "donation.donor_id != donor.id")
        self.donations_table.add_donation(donation)
        if not self.donors_table.donor_exists_in_database(donor.id.value):
            self.donors_table.add_donor(donor)

    def get_donors_names_sorted_per_total_hist_donation_amount(self) -> list:
        id_sorted = self.donations_table.get_donors_id_sorted_per_total_hist_donation_amount()
        return [self.donors_table.get_donor_name(donor_id) for donor_id in id_sorted]
