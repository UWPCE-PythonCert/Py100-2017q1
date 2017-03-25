
from Table import Table


class DonationsTable(Table):

    def __init__(self, table=None):
        if table is not None:
            self.__table = table.copy()
        else:
            self.__table = dict()

    @property
    def table(self) -> dict:
        return self.__table

    def _donor_exists_in_database(self, donor_id: str) -> bool:
        return donor_id in self.table

    def get_per_donor(self, donor_id: str) -> dict:
        if self._donor_exists_in_database(donor_id):
            return self.table[donor_id]
        raise ValueError("ValueError: get_per_donor(donor_id): - "
                         "donor does not exist in the database")

    def _get_dates_per_donor(self, donor_id: str) -> list:
        dates = list(self.get_per_donor(donor_id).keys())
        dates.sort()
        return dates

    from datetime import date

    def get_per_donor_per_date(self, donor_id: str, date: date) -> list:
        if date in self._get_dates_per_donor(donor_id):
            return self.get_per_donor(donor_id)[date]
        raise ValueError("ValueError - "
                         "get_per_donor_per_date(donor_id, date): "
                         "invalid argument. date not in database")

    from Donation import Donation

    def _add_date(self, donation: Donation) -> None:
        self.get_per_donor(donation.donor_id.value)[donation.date] = list()

    def exists_previous_from_donor_same_date(self, donation: Donation) -> bool:
        return donation.date in \
               self._get_dates_per_donor(donation.donor_id.value)

    def _add_donation_existing_date(self, donation: Donation) -> None:
        self.get_per_donor_per_date(donation.donor_id.value, donation.date) \
            .append(donation)

    def _add_donation_new_date(self, donation: Donation) -> None:
        self._add_date(donation)
        self._add_donation_existing_date(donation)

    def _add_donor(self, donor_id: str) -> None:
        donor_id = donor_id
        self.table[donor_id] = dict()

    def _add_donation_from_new_donor(self, donation: Donation) -> None:
        self._add_donor(donation.donor_id.value)
        self._add_date(donation)
        self._add_donation_existing_date(donation)

    def _add_donation_from_existing_donor(self, donation: Donation) -> None:
        donation_new_date = not self.exists_previous_from_donor_same_date(donation)
        if donation_new_date:
            self._add_donation_new_date(donation)
        else:
            self._add_donation_existing_date(donation)

    def add_donation(self, donation: Donation) -> None:
        new_donor = not self._donor_exists_in_database(donation.donor_id.value)
        if new_donor:
            self._add_donation_from_new_donor(donation)
        else:
            self._add_donation_from_existing_donor(donation)

    def _sum_donations_per_donor_per_date(self, donor_id: str, date: date) -> float:
        sum_donations = 0
        for donation in self.get_per_donor_per_date(donor_id, date):
            sum_donations += donation.amount
        return sum_donations

    def get_total_donation_amount_per_donor(self, donor_id: str) -> float:
        total_donation_amount = 0
        for date in self.get_per_donor(donor_id).keys():
            total_donation_amount += self._sum_donations_per_donor_per_date(donor_id, date)
        return total_donation_amount

    def get_total_donations_amounts(self) -> dict:
        tot_don_amounts = dict()
        for donor_id in self.table:
            tot_don_amounts[donor_id] = \
                self.get_total_donation_amount_per_donor(donor_id)
        return tot_don_amounts

    def _get_num_gifts_per_donor_per_date(self, donor_id: str, date: str) -> int:
        return len(self.get_per_donor_per_date(donor_id, date))

    def get_num_gifts_per_donor(self, donor_id: str) -> int:
        num_gifts = 0
        for date in self.get_per_donor(donor_id).keys():
            num_gifts += self._get_num_gifts_per_donor_per_date(donor_id, date)
        return num_gifts

    def get_num_gifts(self) -> dict:
        num_gifts = dict()
        for donor_id in self.table:
            num_gifts[donor_id] = self.get_num_gifts_per_donor(donor_id)
        return num_gifts

    def get_average_gift_per_donor(self, donor_id: str) -> float:
        return self.get_total_donation_amount_per_donor(donor_id) / \
               self.get_num_gifts_per_donor(donor_id)

    def get_average_gift(self) -> dict:
        avge_gift = dict()
        for donor_id in self.table:
            avge_gift[donor_id] = self.get_average_gift_per_donor(donor_id)
        return avge_gift

    def get_donors_id_sorted_per_total_hist_donation_amount(self) -> list:
        total_donations = self.get_total_donations_amounts()
        return sorted(total_donations, key=total_donations.__getitem__)
