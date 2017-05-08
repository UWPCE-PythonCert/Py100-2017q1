
from Person import Person


class OrganisationMember(Person):
    pass


class Organisation:

    from Address import Address
    from Name import OrganisationName
    from OrganisationMembersTable import OrganisationMembersTable
    from Database import Database

    def __init__(self, name: OrganisationName, address: Address, database: Database):
        self.__name = name
        self.__address = address
        self.__db = database

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
    def members(self) -> OrganisationMembersTable:
        return self.__db.organisation_members_table

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.address == other.address

    def add_member(self, member: OrganisationMember) -> None:
        self.members.add_person(member)

    def get_member(self, member_id: str) -> Person:
        return self.members.get_person(member_id)


class OrganisationMember(Person):

    from Name import PersonName
    from Address import Address
    from MyDate import MyDate

    def __init__(self, name: PersonName, address: Address,
                 birth_date: MyDate, organisation: Organisation):
        super(OrganisationMember, self).__init__(name, address, birth_date)
        self.__organisation = organisation
        self.__organisation.add_member(self)

    @property
    def organisation(self):
        return self.__organisation

    def __eq__(self, other) -> bool:
        return super(OrganisationMember, self).__eq__(other)\
               and self.organisation == other.organisation
