
from Table import Table


class DonorsTable(Table):

    from Donor import Donor
    from Name import PersonName

    def __init__(self, table=None):
        if table is not None:
            self.__table = table.copy()
        else:
            self.__table = dict()

    @property
    def table(self) -> dict:
        return self.__table

    def donor_exists_in_database(self, donor_id: str) -> bool:
        return donor_id in self.table

    def _get_donors_id(self) -> tuple:
        return tuple(self.table.keys())

    def get_donor(self, donor_id: str) -> Donor:
        if self.donor_exists_in_database(donor_id):
            return self.table[donor_id]
        raise ValueError("ValueError: get_donor(donor_id): - "
                         "donor does not exist in the database")

    def get_donor_name(self, donor_id: str) -> PersonName:
        return self.get_donor(donor_id).name

    def get_donors_names(self) -> list:
        donors = [donor.name for donor in self.__table.values()]
        donors.sort()
        return donors

    def add_donor(self, donor: Donor) -> None:
        self.table[donor.id.value] = donor
