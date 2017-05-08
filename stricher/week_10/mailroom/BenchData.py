
class DonorsDBBenchData:

    def _init_helper(self, donors: tuple) -> None:

        from Name import PersonName
        from Address import Address
        from Donor import Donor

        for don in donors:
            name = PersonName(prefix=don["prefix"], first=don["first_name"], last=don["last_name"])
            address = Address(street=don["street"], zipcode=don["zipcode"],
                              city=don["city"], country=don["country"],
                              phone=don["phone"], mail=don["email"])
            donor = Donor(name=name, address=address, birth_date=don["birth_date"])
            self.__data[donor.id.value] = donor
            self.__data_list.append(donor)

    def __init__(self):

        self.__data = {}
        self.__data_list = []

        from MyDate import MyDate
        from EmailAddress import EmailAddress
        donors = \
            (
                dict(prefix="M", first_name="Charles", last_name="Ives",
                     street="14, Avenue Foch", zipcode="75016", city="Paris",
                     country="France", phone="+33 1 45 67 83 45",
                     email=EmailAddress("charles.ives@centralparkinthedark.com"),
                     birth_date=MyDate(1874, 10, 20)),
                dict(prefix="M", first_name="Jean S", last_name="Bach",
                     street="4, rue de la paix", zipcode="75008", city="Paris",
                     country="France", phone="+33 1 42 67 78 34",
                     email=EmailAddress("js.bach@google.com"),
                     birth_date=MyDate(1685, 3, 31)),
                dict(prefix="M", first_name="Lee", last_name="Morgan",
                     street="153, boulevard Saint-Germain", zipcode="75006", city="Paris",
                     country="France", phone="+33 1 46 78 09 45",
                     email=EmailAddress("lee.morgan@jazzmessengers.com"),
                     birth_date=MyDate(1938, 7, 10)),
                dict(prefix="M", first_name="Miles", last_name="Davis",
                     street="154, boulevard Saint-Germain", zipcode="75006", city="Paris",
                     country="France", phone="+33 1 45 67 33 12",
                     email=EmailAddress("miles.davis@myself.com"),
                     birth_date=MyDate(1926, 5, 26)),
                dict(prefix="M", first_name="Wynton", last_name="Kelly",
                     street="3, place du Tertre", zipcode="75018", city="Paris",
                     country="France", phone="+33 1 45 87 34 25",
                     email=EmailAddress("wynton.kelly@quintet.com"),
                     birth_date=MyDate(1931, 12, 2)),
                dict(prefix="Ms", first_name="Eliane", last_name="Radigue",
                     street="23, rue de Seine", zipcode="75006", city="Paris",
                     country="France", phone="+33 1 46 78 94 67",
                     email=EmailAddress("eliane.radigue@ircam.com"),
                     birth_date=MyDate(1932, 1, 24))
            )
        self._init_helper(donors)

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def data_list(self) -> list:
        return self.__data_list

    def __repr__(self) -> str:
        counter = 0
        str = ""
        for donor_id, donor_name in self.data.items():
            str += "" if counter == 0 else "\n"
            counter += 1
            str += "{}: {} {}".format(donor_id, donor_name[0], donor_name[1])
        return str


class DonationsDBBenchData:

    from Donor import Donor
    from MyDate import MyDate

    def __init_helper(self, donor: Donor, donation_date: MyDate, amount: float) -> None:

        from Donation import Donation

        donation = Donation(donor, donation_date, amount, DatabaseBench.db)

        def __helper(donation: Donation):
            if donation.donor.id.value not in self.__data:
                self.__data[donation.donor.id.value] = {}
            if donation.date not in self.__data[donation.donor.id.value]:
                self.__data[donation.donor.id.value][donation.date] = []
            self.__data[donation.donor.id.value][donation.date].append(donation)

        __helper(donation)

    def __init__(self):

        self.__data = {}

        from PersonId import PersonId
        from MyDate import MyDate
        from EmailAddress import EmailAddress

        donors_db = DonorsDBBenchData().data

        donor = donors_db[PersonId(EmailAddress("charles.ives@centralparkinthedark.com")).value]
        donation_dates = [MyDate(2012, 4, 12), MyDate(2014, 2, 8)]
        amounts = [[567, 1000], 7654]
        self.__init_helper(donor, donation_dates[0], amounts[0][0])
        self.__init_helper(donor, donation_dates[0], amounts[0][1])
        self.__init_helper(donor, donation_dates[1], amounts[1])

        donor = donors_db[PersonId(EmailAddress("js.bach@google.com")).value]
        donation_dates = [MyDate(2014, 8, 6), MyDate(2011, 12, 25), MyDate(2016, 4, 1)]
        amounts = [2897, 4567, 876]
        self.__init_helper(donor, donation_dates[0], amounts[0])
        self.__init_helper(donor, donation_dates[1], amounts[1])
        self.__init_helper(donor, donation_dates[2], amounts[2])

        donor = donors_db[PersonId(EmailAddress("lee.morgan@jazzmessengers.com")).value]
        donation_dates = [MyDate(2015, 10, 23), MyDate(2016, 10, 14)]
        amounts = [3567, 7167]
        self.__init_helper(donor, donation_dates[0], amounts[0])
        self.__init_helper(donor, donation_dates[1], amounts[1])

        donor = donors_db[PersonId(EmailAddress("miles.davis@myself.com")).value]
        donation_dates = [MyDate(2011, 5, 19)]
        amounts = [67000, 15000]
        self.__init_helper(donor, donation_dates[0], amounts[0])
        self.__init_helper(donor, donation_dates[0], amounts[1])

        donor = donors_db[PersonId(EmailAddress("wynton.kelly@quintet.com")).value]
        donation_dates = [MyDate(2009, 2, 24), MyDate(2007, 6, 18), MyDate(2013, 4, 5)]
        amounts = [7894, 6666, 657]
        self.__init_helper(donor, donation_dates[0], amounts[0])
        self.__init_helper(donor, donation_dates[1], amounts[1])
        self.__init_helper(donor, donation_dates[2], amounts[2])

        donor = donors_db[PersonId(EmailAddress("eliane.radigue@ircam.com")).value]
        donation_dates = [MyDate(2016, 1, 7)]
        amounts = [8000]
        self.__init_helper(donor, donation_dates[0], amounts[0])

    @staticmethod
    def get_donations_list_from_raw_data(email: str,
                                         donation_dates: list,
                                         donation_amounts: list) -> list:

        from PersonId import PersonId
        from EmailAddress import EmailAddress
        from Donation import Donation

        db = DatabaseBench.db
        donor = DonorsDBBenchData().data[PersonId(EmailAddress(email)).value]
        donations_list = []
        for date, amounts in zip(donation_dates, donation_amounts):
            if type(amounts) == list:
                for amount in amounts:
                    donations_list.append(Donation(donor, date, amount, db))
            else:
                donations_list.append(Donation(donor, date, amounts, db))
        return donations_list

    def get_donations_list_from_bench_db(self, email: str):

        from PersonId import PersonId
        from EmailAddress import EmailAddress

        def get_donor_id_str():
            return PersonId(EmailAddress(email)).value

        donations_from_donor = self.data[get_donor_id_str()]
        donations_list = []
        for donations_per_date in donations_from_donor.values():
            if type(donations_per_date) == list:
                for donation in donations_per_date:
                    donations_list.append(donation)
            else:
                donations_list.append(donations_per_date)
        return donations_list

    @property
    def data(self):
        return self.__data


class DatabaseBench:

    from Database import Database
    db = Database()

    def __init__(self):
        donations_bench = DonationsDBBenchData()
        donors_bench_data = DonorsDBBenchData().data
        for donor in donors_bench_data.values():
            email = donor.mail.get
            donations_bench_list = donations_bench.get_donations_list_from_bench_db(email)
            for donation in donations_bench_list:
                donation.add_to_database()


class OrganisationBenchData:

    def __init__(self):
            self.__data = OrganisationBenchData.__init_helper()

    @staticmethod
    def __init_helper():
        from Organisation import OrganisationMember
        from Name import OrganisationName
        from Organisation import Organisation
        from Address import Address
        from Database import Database
        from Name import PersonName
        from MyDate import MyDate
        from EmailAddress import EmailAddress

        db = Database()

        name = OrganisationName("MusicFactory")
        address = Address("14, rue Beaune", "75007",
                          "Paris", "France",
                          "+33 1 43 56 78 23",
                          EmailAddress("music.factory@drummachine.net"))
        music_factory = Organisation(name=name, address=address, database=db)

        cat_anderson = OrganisationMember(name=PersonName("M", "Cat", "Anderson"),
                                          address=address, birth_date=MyDate(1916, 9, 12),
                                          organisation=music_factory)

        clifford_brown = OrganisationMember(name=PersonName("M", "Clifford", "Brown"),
                                            address=address, birth_date=MyDate(1930, 10, 30),
                                            organisation=music_factory)

        return music_factory

    @property
    def data(self):
        return self.__data


class MenuBenchData:
    @staticmethod
    def get_quit_message() -> str:
        return "\n\nThe program quits. Goodbye!\n"


class HomeMenuBenchData(MenuBenchData):

    @staticmethod
    def get_request_to_user() -> str:
        return "\nPlease choose one of the following actions (1-2-3-4):\n\n"

    @staticmethod
    def get_menu() -> str:
        return "(1) Display the donations menu\n" \
               "(2) Send a thank you email\n" \
               "(3) Create a report\n" \
               "(4) quit\n\n"

    @staticmethod
    def get_input_str() -> str:
        return "Enter: "

    @staticmethod
    def get_menu_error_message() -> str:
        return "\nInvalid input. Please enter a number between 1 and 4!\n"


class TestThat:
    __doTest = False
    __registered = dict(thank_you="in send_a_thank_you_email()\n",
                        create_report="in create_report()\n",
                        quit_program="in quit_program()\n")

    def register(self, method, trace):
        self.__registered[method] = trace

    def get_trace(self, method) -> str:
        return self.__registered[method]

    def do(self) -> bool:
        return self.__doTest
