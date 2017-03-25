
from Person import Person


class OrganisationMember(Person):
    pass


class Organisation:

    from Address import Address
    from Name import OrganisationName
    from PersonId import PersonId

    def __init__(self, name: OrganisationName, address: Address):
        self.__name = name
        self.__address = address
        self.__members = dict()

    def __repr__(self) -> str:
        return "Organisation({},{})".\
            format(self.name.__repr__(), self.address.__repr__())

    @property
    def name(self) -> OrganisationName:
        return self.__name

    @property
    def address(self) -> Address:
        return self.__address

    @property
    def members(self) -> dict:
        return self.__members

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.address == other.address

    def add_member(self, member: OrganisationMember) -> None:
        self.members[member.id.value] = member

    def get_member(self, member_id: PersonId) -> OrganisationMember:
        return self.members[member_id.value]


class OrganisationMember(Person):

    from Name import PersonName
    from Address import Address
    from datetime import date

    def __init__(self, name: PersonName, address: Address,
                 birth_date: date, organisation: Organisation):
        super(OrganisationMember, self).__init__(name, address, birth_date)
        self.__organisation = organisation
        self.__organisation.add_member(self)

    @property
    def organisation(self):
        return self.__organisation

    def __eq__(self, other) -> bool:
        return super(OrganisationMember, self).__eq__(other)\
               and self.organisation == other.organisation
