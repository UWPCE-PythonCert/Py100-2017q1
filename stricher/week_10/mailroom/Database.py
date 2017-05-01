from enum import Enum

from DatabaseError import DatabaseError


class DBWriterType(Enum):

    sql_lite = 0
    sql_server = 1


class Database:

    from Person import Person
    from PersonId import PersonId
    from MyDate import MyDate
    from Donation import Donation
    from DonorsTable import DonorsTable
    from DonationsTable import DonationsTable
    from OrganisationMembersTable import OrganisationMembersTable

    def __init__(self):
        from DonorsTable import DonorsTable
        from DonationsTable import DonationsTable
        from OrganisationMembersTable import OrganisationMembersTable
        self.__donors_table = DonorsTable()
        self.__donations_table = DonationsTable()
        self.__organisation_members_table = OrganisationMembersTable()

    @property
    def donors_table(self) -> DonorsTable:
        return self.__donors_table

    @property
    def donations_table(self) -> DonationsTable:
        return self.__donations_table

    @property
    def organisation_members_table(self) -> OrganisationMembersTable:
        return self.__organisation_members_table

    def __str__(self):
        return "Database: TO_IMPLEMENT"

    def add_donation(self, donation: Donation) -> None:
        if self.donation_exists(donation):
            raise DatabaseError("Database.add_donation(donation)"
                                " - donation already exists in the database")
        self.donations_table.add_donation(donation)
        if not self.donors_table.person_exists_in_database(donation.donor.id.value):
            self.donors_table.add_person(donation.donor)

    def get_donation(self, donor_id: PersonId, donation_date: MyDate) -> list:
        return self.donations_table.get_per_donor_per_date(donor_id.value, donation_date)

    def get_donors_names_sorted_per_total_hist_donation_amount(self) -> list:
        id_sorted = self.donations_table.get_donors_id_sorted_per_total_hist_donation_amount()
        return [self.donors_table.get_person_name(donor_id) for donor_id in id_sorted]

    def donor_exists(self, donor_id: str) -> bool:
        return self.donors_table.person_exists_in_database(donor_id)

    def get_donor(self, donor_id=None, mail=None) -> Person:
        if donor_id is None or mail is None:
            raise DatabaseError("Database.get_donor(donor_id, mail). "
                                "Missing argument donor_id or mail")
        if donor_id is not None:
            return self.donors_table.get_person(donor_id)
        from PersonId import PersonId
        from EmailAddress import EmailAddress
        return self.donors_table.get_person(PersonId(EmailAddress(mail)).value)

    def donation_exists(self, donation: Donation) -> bool:
        return self.donations_table.exists_previous_donation(donation)

    def write(self, writer_type: DBWriterType) -> None:
        factory = DatabaseWriterFactory()
        db_writer = factory.get_writer(writer_type)
        db_writer.write(self)


class DatabaseWriter:
    @staticmethod
    def write(database: Database) -> None:
        pass


class DatabaseWriterToFile(DatabaseWriter):
    def __init__(self):
        super(DatabaseWriterToFile, self).__init__()


class DatabaseWriterToRDBMS(DatabaseWriter):
    def __init__(self):
        super(DatabaseWriterToRDBMS, self).__init__()


class DatabaseWriterToSQLite(DatabaseWriterToRDBMS):
    def __init__(self):
        super(DatabaseWriterToSQLite, self).__init__()

    @staticmethod
    def write(database: Database) -> None:
        # TODO: implement
        pass


class DatabaseWriterToSQLServer(DatabaseWriterToRDBMS):
    def __init__(self):
        super(DatabaseWriterToSQLServer, self).__init__()

    @staticmethod
    def write(database: Database) -> None:
        # TODO: implement
        pass


class DatabaseWriterFactory:
    def __init__(self):
        self.__writers = dict(sql_lite=DatabaseWriterToSQLite(),
                              sql_server=DatabaseWriterToSQLServer())

    def get_writer(self, writer_type: DBWriterType) -> DatabaseWriter:
        return self.__writers[writer_type.name]
