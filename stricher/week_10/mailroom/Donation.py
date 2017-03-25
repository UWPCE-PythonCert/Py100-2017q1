
class Donation:

    from PersonId import PersonId
    from datetime import date

    #TODO: replace PersonId by Donor (store a reference to Donor) and record donation to the Database automatically from Donation's constructor

    def __init__(self, donor_id: PersonId, donation_date: date, amount: float):
        self.__donor_id = donor_id
        self.__date = donation_date
        self.__amount = amount

    def __eq__(self, other):
        return self.donor_id == other.donor_id\
               and self.date == other.date\
               and self.amount == other.amount

    def __str__(self):
        return "{}: {} - {}".format(self.donor_id.value, self.date, self.amount)

    @property
    def donor_id(self) -> PersonId:
        return self.__donor_id

    @property
    def date(self) -> date:
        return self.__date

    @property
    def amount(self) -> float:
        return self.__amount

    def get_attr(self, attr_str: str):
        return getattr(self, attr_str)
