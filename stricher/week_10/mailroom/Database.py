from enum import Enum


class DBWriterType(Enum):

    sql_lite = 0
    sql_server = 1


class Database:

    from Donation import Donation
    from Donor import Donor
    from PersonId import PersonId
    from DonorsTable import DonorsTable
    from DonationsTable import DonationsTable
    from datetime import date

    def __init__(self, donors_table=None, donations_table=None):

        if donors_table is None and donations_table is None:
            from DonorsTable import DonorsTable
            from DonationsTable import DonationsTable

            self.__donors_table = DonorsTable()
            self.__donations_table = DonationsTable()

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

    def __str__(self):
        return "Database: TO_IMPLEMENT"

    def add_donation(self, donation: Donation, donor: Donor) -> None:
        if donation.donor_id != donor.id:
            raise ValueError("ValueError - Database.add_donation(donation, donor): "
                             "donation.donor_id != donor.id")
        self.donations_table.add_donation(donation)
        if not self.donors_table.donor_exists_in_database(donor.id.value):
            self.donors_table.add_donor(donor)

    def get_donation(self, donor_id: PersonId, donation_date: date) -> list:
        return self.donations_table.get_per_donor_per_date(donor_id.value, donation_date)

    def get_donors_names_sorted_per_total_hist_donation_amount(self) -> list:
        id_sorted = self.donations_table.get_donors_id_sorted_per_total_hist_donation_amount()
        return [self.donors_table.get_donor_name(donor_id) for donor_id in id_sorted]

    def donor_exists(self, donor_id: str) -> bool:
        return self.donors_table.donor_exists_in_database(donor_id)

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
