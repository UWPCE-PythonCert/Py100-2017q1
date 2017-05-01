
from TextGenerator import TextGenerator


class EmailGenerator(TextGenerator):
    def __init__(self):
        super(EmailGenerator, self).__init__()


class EmailDonationsGenerator(EmailGenerator):

    from Database import Database
    from Donation import Donation
    from PersonId import PersonId
    from Person import Person
    from Organisation import Organisation

    def __init__(self, donations_db: Database, donation: Donation,
                 author_id: PersonId, organisation: Organisation):

        if not donations_db.donors_table.person_exists_in_database(donation.donor_id.value):
            raise ValueError("ValueError - "
                             "EmailDonationsGenerator(db,"
                             " donation, author_id): donor not in database")
        if not organisation.members.person_exists_in_database(author_id.value):
            raise ValueError("ValueError - "
                             "EmailDonationsGenerator(db,"
                             " donation, author_id): author not in database")
        if not donations_db.donations_table.exists_previous_from_donor_same_date(donation):
            raise ValueError("ValueError - "
                             "EmailDonationsGenerator(db,"
                             " donation, author_id): donation not in database")
        self.__db = donations_db
        self.__donation = donation
        self.__author_id = author_id
        self.__organisation = organisation
        super(EmailDonationsGenerator, self).__init__()

    @property
    def db(self):
        return self.__db

    @property
    def donation(self):
        return self.__donation

    @property
    def author_id(self):
        return self.__author_id

    @property
    def organisation(self):
        return self.__organisation

    def author(self) -> Person:
        return self.organisation.get_member(self.author_id.value)

    def _donor_id(self) -> str:
        return self.donation.donor_id.value

    def recipient(self) -> Person:
        return self.db.get_donor(self._donor_id())

    def _generate(self) -> str:
        recipient = self.recipient()
        name = str(recipient.name)
        address = str(recipient.address)
        message = "Dear {}, \n\nThank you very much for your donation.\n\n" \
                  "Yours sincerely,\n\n{}\n".format(name, self.author)
        string = "\n{}\n{}\n{}\n".format(name, address, message)
        return string
