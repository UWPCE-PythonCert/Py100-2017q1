
from Id import Id


class PersonId(Id):

    from Name import PersonName
    from datetime import date

    def __init__(self, name: PersonName, birth_date: date):
        self.__value = self.get_hash(name.full_name.upper()
                                     + str(birth_date))

    def __eq__(self, other):
        return self.value == other.value

    @property
    def value(self):
        return self.__value
