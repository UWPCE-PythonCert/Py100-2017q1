

class TextGenerator:

    def __init__(self):
        self.__str = self._generate()

    def __str__(self):
        return self.__str

    def _generate(self) -> str:
        pass

    from sys import stdout

    def write(self, ostream=stdout) -> None:
        ostream.write(self.__str)


class ReportGenerator(TextGenerator):

    def __init__(self):
        super(ReportGenerator, self).__init__()


class ReportDonationsDBGenerator(ReportGenerator):

    from Database import Database

    def __init__(self, donations_db: Database):
        self.__db = donations_db
        super(ReportDonationsDBGenerator, self).__init__()

    def _generate(self) -> str:
        donors_id = self.__db.donations_table.get_donors_id_sorted_per_total_hist_donation_amount()

        total_donation_per_donor = self.__db.donations_table.get_total_donations_amounts()
        num_donations_per_donor = self.__db.donations_table.get_num_gifts()
        avge_donation_per_donor = self.__db.donations_table.get_average_gift()

        string = "\nList of donors:\n\n"
        string += 99 * '*' + '\n'
        string += '{:^20}'.format('Name') + '|'\
                  + '{:^30}'.format('Total amount') + '|' \
                  + '{:^25}'.format('Number of donations') + '|' \
                  + '{:^20}'.format('Average donation') + '|'\
                  + '\n'
        string += 99 * '*' + '\n'
        ii = 0
        for don_id in donors_id:
            string += "" if ii == 0 else "\n"
            name = str(self.__db.donors_table.get_donor_name(don_id))
            string += '{:20}'.format(name) + '|'
            string += '{:>30.2f}'.format(total_donation_per_donor[don_id]) + '|'
            string += '{:>25}'.format(num_donations_per_donor[don_id]) + '|'
            string += '{:>20.2f}'.format(avge_donation_per_donor[don_id]) + '|'
            ii += 1
        string += '\n'
        string += 99 * '*' + '\n'
        return string


class EmailGenerator(TextGenerator):
    def __init__(self):
        super(EmailGenerator, self).__init__()


class EmailDonationsGenerator(EmailGenerator):

    from Database import Database
    from Donation import Donation

    def __init__(self, donations_db: Database, donation: Donation, author: str):
        self.__db = donations_db
        if not self.__db.donors_table.donor_exists_in_database(donation.donor_id.value):
            raise ValueError("ValueError - "
                             "EmailDonationsGenerator(donations_db,"
                             " donor_id, donation_date): donor not in database")
        if not self.__db.donations_table.exists_previous_from_donor_same_date(donation):
            raise ValueError("ValueError - "
                             "EmailDonationsGenerator(donations_db,"
                             " donor_id, donation_date): donation not in database")
        self.__donation = donation
        self.__author = author
        super(EmailDonationsGenerator, self).__init__()

    @property
    def db(self):
        return self.__db

    @property
    def donation(self):
        return self.__donation

    @property
    def author(self):
        return self.__author

    def _generate(self) -> str:
        donor = self.db.donors_table.get_donor(self.donation.donor_id.value)
        name = str(donor.name)
        address = str(donor.address)
        message = "Dear {}, \n\nThank you very much for your donation.\n\nYours sincerely,\n\n{}\n".format(name, self.author)
        string = "\n{}\n{}\n{}\n".format(name, address, message)
        return string

