
from Person import Person


class Donor(Person):

    from Name import Name
    from Address import Address
    from datetime import date
    from DonorId import DonorId

    def __init__(self, name: Name, address: Address,
                 birth_date: date):
        super(Donor, self).__init__(name, address, birth_date)
        from DonorId import DonorId
        self.__id = DonorId(self.name, self.birth_date)

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self) -> DonorId:
        return self.__id
