

class DonationError(ValueError):

    def __init__(self, message: str):
        super(DonationError, self).__init__("DonationError: " + message)


class Donation:

    from Donor import Donor
    from MyDate import MyDate

    def __init__(self, donor: Donor, donation_date, amount: float,
                 database):

        from MyDate import MyDate

        if isinstance(donation_date, str):
            splitted_str = donation_date.split("-")
            try:
                year = int(splitted_str[0])
                month = int(splitted_str[1])
                day = int(splitted_str[2])
            except ValueError as ve:
                raise DonationError("Donation(donor,"
                                    " donation_date, amount)"
                                    " - {}".format(str(ve)))
            donation_date = MyDate(year, month, day)

        elif not isinstance(donation_date, MyDate):
            raise DonationError("Donation(donor, donation_date, amount) - "
                                "donation_date must be either of type string or MyDate")

        if amount <= 0:
            raise DonationError("Donation(donor, donation_date, amount)"
                                " - amount must be strictly positive")
        self.__donor = donor
        self.__date = donation_date
        self.__amount = amount
        self.__database = database

    def __eq__(self, other):
        return self.donor == other.donor\
               and self.date == other.date\
               and self.amount == other.amount

    def __str__(self):
        return "\nDonor:\n------\n{}\nDonation:\n---------\n{}: {}".\
            format(self.donor, self.date, self.amount)

    @property
    def donor(self) -> Donor:
        return self.__donor

    @property
    def date(self) -> MyDate:
        return self.__date

    @property
    def amount(self) -> float:
        return self.__amount

    def get_attr(self, attr_str: str):
        return getattr(self, attr_str)

    def add_to_database(self):
        self.__database.add_donation(self)
