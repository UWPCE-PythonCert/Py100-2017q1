
class Person:

    from Name import PersonName
    from Address import Address
    from datetime import date
    from PersonId import PersonId

    def __init__(self, name: PersonName, address: Address,
                 birth_date: date):
        from PersonId import PersonId
        self.__name = name
        self.__address = address
        self.__birth_date = birth_date
        self.__id = PersonId(self.name, self.birth_date)

    def __repr__(self):
        return 'Person({},{},{})'.format(self.name.__repr__(),
                                         self.address.__repr__(),
                                         self.birth_date.__repr__())

    def __str__(self):
        return "{}\n{}".format(self.name, self.address)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    @property
    def name(self) -> PersonName:
        return self.__name

    @property
    def address(self) -> Address:
        return self.__address

    @property
    def birth_date(self) -> date:
        return self.__birth_date

    @property
    def id(self) -> PersonId:
        return self.__id
