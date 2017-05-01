from Table import Table


class DonationsTable(Table):
    from MyDate import MyDate
    from Donation import Donation
    from sys import stdout

    def __init__(self, table=None):
        super(DonationsTable, self).__init__(table)

    def _donor_exists_in_database(self, donor_id: str) -> bool:
        return donor_id in self.table

    def get_per_donor(self, donor_id: str) -> dict:
        from DatabaseError import DatabaseError
        if self._donor_exists_in_database(donor_id):
            return self.table[donor_id]
        raise DatabaseError("DatabaseError: get_per_donor(donor_id): - "
                            "donor does not exist in the database")

    def _get_dates_per_donor(self, donor_id: str) -> list:
        dates = list(self.get_per_donor(donor_id).keys())
        dates.sort()
        return dates

    def get_per_donor_per_date(self, donor_id: str, date: MyDate) -> list:
        from DatabaseError import DatabaseError
        if date in self._get_dates_per_donor(donor_id):
            return self.get_per_donor(donor_id)[date]
        raise DatabaseError("DatabaseError - "
                            "get_per_donor_per_date(donor_id, date): "
                            "invalid argument. date not in database")

    def _add_date(self, donation: Donation) -> None:
        self.get_per_donor(donation.donor.id.value)[donation.date] = list()

    def exists_previous_from_donor_same_date(self, donation: Donation) -> bool:
        return donation.date in \
               self._get_dates_per_donor(donation.donor.id.value)

    def exists_previous_donation(self, donation: Donation) -> bool:
        from DatabaseError import DatabaseError
        try:
            exists = donation in \
                     self.get_per_donor_per_date(donation.donor.id.value, donation.date)
        except DatabaseError:
            exists = False
        return exists

    def _add_donation_existing_date(self, donation: Donation) -> None:
        self.get_per_donor_per_date(donation.donor.id.value, donation.date) \
            .append(donation)

    def _add_donation_new_date(self, donation: Donation) -> None:
        self._add_date(donation)
        self._add_donation_existing_date(donation)

    def _add_donor(self, donor_id: str) -> None:
        donor_id = donor_id
        self.table[donor_id] = dict()

    def _add_donation_from_new_donor(self, donation: Donation) -> None:
        self._add_donor(donation.donor.id.value)
        self._add_date(donation)
        self._add_donation_existing_date(donation)

    def _add_donation_from_existing_donor(self, donation: Donation) -> None:
        donation_new_date = not self.exists_previous_from_donor_same_date(donation)
        if donation_new_date:
            self._add_donation_new_date(donation)
        else:
            self._add_donation_existing_date(donation)

    def add_donation(self, donation: Donation) -> None:
        new_donor = not self._donor_exists_in_database(donation.donor.id.value)
        if new_donor:
            self._add_donation_from_new_donor(donation)
        else:
            self._add_donation_from_existing_donor(donation)

    def _sum_donations_per_donor_per_date(self, donor_id: str, date: MyDate) -> float:
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

    def _get_num_gifts_per_donor_per_date(self, donor_id: str, date: MyDate) -> int:
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

#TODO: fix bug
    def write_donations_given_donor(self, email=None, donor_id=None, ostream=stdout,
                                    border_char='.', sep_char='.', counter=0) -> None:

        from Donation import Donation
        from PersonId import PersonId

        if email is None and donor_id is None:
            raise ValueError('ValueError: DonationsTable.'
                             'write_donations_given_donor'
                             '(email, donor_id, ostream) - '
                             'missing argument email or donor_id')
        if donor_id is None:
            donor_id = PersonId(email).value

        donations_from_donor = self.table[donor_id]
        num_donations = self.get_num_gifts_per_donor(donor_id)

        def __donation_string(donation: Donation, border_char: str,
                              sep_char: str, counter: int) -> str:
            header_border = '{} {} {}'.format(15 * '*', donation.donor.name, 15 * '*')
            border = 40 * border_char
            sep = '{}{}{}'.format(18 * ' ', counter + 1, 18 * ' ')
            if counter == 0:
                return '\n{}\n{}\n\n{}\n{}'.format(header_border, sep, str(donation), border)
            elif counter == num_donations - 1:
                return '\n{}\n{}\n{}'.format(sep, border, str(donation))
            else:
                return '\n\n{}\n{}\n\n{}\n{}'.format(sep, border, str(donation), border)

        for donations_per_date in donations_from_donor.values():
            if type(donations_per_date) == list:
                for donation in donations_per_date:
                    ostream.write(__donation_string(donation, border_char=border_char,
                                                    sep_char=sep_char, counter=counter))
                    counter += 1
            else:
                ostream.write(__donation_string(donation, border_char=border_char,
                                                sep_char=sep_char, counter=counter))
                counter += 1

    def write(self, ostream=stdout, border_char='.', sep_char='.') -> None:
        for counter, donor_id in enumerate(self.table.keys()):
            self.write_donations_given_donor(donor_id=donor_id, ostream=ostream,
                                             border_char=border_char, sep_char=sep_char)
