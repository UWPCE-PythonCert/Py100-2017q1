

class DonorsDBBenchData:

    def _init_helper(self, donors: tuple) -> None:

        from Name import Name
        from Address import Address
        from Donor import Donor

        for don in donors:
            name = Name(prefix=don["prefix"], first=don["first_name"], last=don["last_name"])
            address = Address(street=don["street"], zipcode=don["zipcode"],
                              city=don["city"], country=don["country"],
                              phone=don["phone"], mail=don["email"])
            donor = Donor(name=name, address=address, birth_date=don["birth_date"])
            self.__data[donor.id.value] = donor

    def __init__(self):

        self.__data = __data = {}

        from datetime import date
        donors = \
            (
                dict(prefix="M", first_name="Charles", last_name="Ives",
                     street="14, Avenue Foch", zipcode="75016", city="Paris",
                     country="France", phone="+33 1 45 67 83 45",
                     email="charles.ives@centralparkinthedark.com", birth_date=date(1874, 10, 20)),
                dict(prefix="M", first_name="Jean S", last_name="Bach",
                    street="4, rue de la paix", zipcode="75008", city="Paris",
                    country="France", phone="+33 1 42 67 78 34",
                     email="js.bach@google.com", birth_date=date(1685, 3, 31)),
                dict(prefix="M", first_name="Lee", last_name="Morgan",
                    street="153, boulevard Saint-Germain", zipcode="75006", city="Paris",
                    country="France", phone="+33 1 46 78 09 45",
                     email="lee.morgan@jazzmessengers.com", birth_date=date(1938, 7, 10)),
                dict(prefix="M", first_name="Miles", last_name="Davis",
                    street="154, boulevard Saint-Germain", zipcode="75006", city="Paris",
                    country="France", phone="+33 1 45 67 33 12",
                     email="miles.davis@myself.com", birth_date=date(1926, 5, 26)),
                dict(prefix="M", first_name="Wynton", last_name="Kelly",
                    street="3, place du Tertre", zipcode="75018", city="Paris",
                    country="France", phone="+33 1 45 87 34 25",
                     email="wynton.kelly@quintet.com", birth_date=date(1931, 12, 2)),
                dict(prefix="Ms", first_name="Eliane", last_name="Radigue",
                     street="23, rue de Seine", zipcode="75006", city="Paris",
                    country="France", phone="+33 1 46 78 94 67",
                     email="eliane.radigue@ircam.com", birth_date=date(1932, 1, 24))
            )
        self._init_helper(donors)

    @property
    def data(self) -> dict:
        return self.__data

    def __repr__(self) -> str:
        counter = 0
        str = ""
        for donor_id, donor_name in self.data.items():
            str += "" if counter == 0 else "\n"
            counter += 1
            str += "{}: {} {}".format(donor_id, donor_name[0], donor_name[1])
        return str


class DonationsDBBenchData:

    from DonorId import DonorId
    from datetime import date

    def __init_helper(self, donor_id: DonorId, donation_date: date, amount: float) -> None:

        from Donation import Donation

        def __helper(donation: Donation):
            if donation.donor_id.value not in self.__data:
                self.__data[donation.donor_id.value] = {}
            if donation.date not in self.__data[donation.donor_id.value]:
                self.__data[donation.donor_id.value][donation.date] = []
            self.__data[donation.donor_id.value][donation.date].append(donation)

        donation = Donation(donor_id, donation_date, amount)
        __helper(donation)

    def __init__(self):

        self.__data = __data = {}

        from DonorId import DonorId
        from datetime import date
        from Name import Name

        donor_id = DonorId(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        donation_dates = [date(2012, 4, 12), date(2014, 2, 8)]
        amounts = [[567, 1000], 7654]
        self.__init_helper(donor_id, donation_dates[0], amounts[0][0])
        self.__init_helper(donor_id, donation_dates[0], amounts[0][1])
        self.__init_helper(donor_id, donation_dates[1], amounts[1])

        donor_id = DonorId(Name("M", "Jean S", "Bach"), date(1685, 3, 31))
        donation_dates = [date(2014, 8, 6), date(2011, 12, 25), date(2016, 4, 1)]
        amounts = [2897, 4567, 876]
        self.__init_helper(donor_id, donation_dates[0], amounts[0])
        self.__init_helper(donor_id, donation_dates[1], amounts[1])
        self.__init_helper(donor_id, donation_dates[2], amounts[2])

        donor_id = DonorId(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        donation_dates = [date(2015, 10, 23), date(2016, 10, 14)]
        amounts = [3567, 7167]
        self.__init_helper(donor_id, donation_dates[0], amounts[0])
        self.__init_helper(donor_id, donation_dates[1], amounts[1])

        donor_id = DonorId(Name("M", "Miles", "Davis"), date(1926, 5, 26))
        donation_dates = [date(2011, 5, 19)]
        amounts = [67000, 15000]
        self.__init_helper(donor_id, donation_dates[0], amounts[0])
        self.__init_helper(donor_id, donation_dates[0], amounts[1])

        donor_id = DonorId(Name("M", "Wynton", "Kelly"), date(1931, 12, 2))
        donation_dates = [date(2009, 2, 24), date(2007, 6, 18), date(2013, 4, 5)]
        amounts = [7894, 6666, 657]
        self.__init_helper(donor_id, donation_dates[0], amounts[0])
        self.__init_helper(donor_id, donation_dates[1], amounts[1])
        self.__init_helper(donor_id, donation_dates[2], amounts[2])

        donor_id = DonorId(Name("Ms", "Eliane", "Radigue"), date(1932, 1, 24))
        donation_dates = [date(2016, 1, 7)]
        amounts = [8000]
        self.__init_helper(donor_id, donation_dates[0], amounts[0])


    @property
    def data(self):
        return self.__data


class MenuBenchData:
    @staticmethod
    def get_quit_message() -> str:
        return "\n\nInvalid entry. Maximum" \
               " number of allowed trials reached (3).\n"


class HomeMenuBenchData(MenuBenchData):
    @staticmethod
    def get_request_to_user() -> str:
        return "\nPlease choose one of the following actions (1-2-3):\n\n"

    @staticmethod
    def get_menu() -> str:
        return "(1) Send a Thank you\n(2) Create a report\n(3) quit\n\n"

    @staticmethod
    def get_input_str() -> str:
        return "Enter: "

    @staticmethod
    def get_menu_error_message() -> str:
        return "\n\nInvalid input. Please enter a number between 1 and 3!\n"


class TestThat:

    __doTest = False
    __registered = dict(thank_you="in thank_you()\n",
                        create_report="in create_report()\n",
                        quit_program="in quit_program()\n")

    def register(self, method, trace):
        self.__registered[method] = trace

    def get_trace(self, method) -> str:
        return self.__registered[method]

    def do(self) -> bool:
        return self.__doTest


