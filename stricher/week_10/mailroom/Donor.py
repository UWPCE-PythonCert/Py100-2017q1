
from Person import Person


class Donor(Person):

    from Name import PersonName
    from Address import Address
    from MyDate import MyDate

    def __init__(self, name: PersonName, address: Address,
                 birth_date: MyDate):
        super(Donor, self).__init__(name, address, birth_date)