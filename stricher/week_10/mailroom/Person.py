
class Person:

    from Name import Name
    from Address import Address
    from datetime import date

    def __init__(self, name: Name, address: Address,
                 birth_date: date):
        self.__name = name
        self.__address = address
        self.__birth_date = birth_date

    def __repr__(self):
        return 'Person({},{},{})'.format(self.name.__repr__(),
                                         self.address.__repr__(),
                                         self.birth_date.__repr__())

    def __str__(self):
        return "{}\n{}".format(self.name, self.address)

    def __eq__(self, other):
        return self.name == other.name \
               and self.address == other.address\
               and self.birth_date == other.birth_date

    @property
    def name(self) -> Name:
        return self.__name

    @property
    def address(self) -> Address:
        return self.__address

    @property
    def birth_date(self) -> date:
        return self.__birth_date
