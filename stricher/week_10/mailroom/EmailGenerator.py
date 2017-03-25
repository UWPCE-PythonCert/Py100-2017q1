
from TextGenerator import TextGenerator

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