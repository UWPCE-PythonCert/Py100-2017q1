
from Id import Id


class DonorId(Id):

    from Name import Name
    from datetime import date

    def __init__(self, name: Name, birth_date: date):
        self.__value = self._get_hash(name.full_name.upper()
                                      + str(birth_date))

    def __eq__(self, other):
        return self.value == other.value

    @property
    def value(self):
        return self.__value
