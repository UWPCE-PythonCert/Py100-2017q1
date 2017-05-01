
from Id import Id


class PersonId(Id):

    from EmailAddress import EmailAddress

    def __init__(self, email: EmailAddress):
        self.__value = self.get_hash(email.get.upper())

    def __eq__(self, other):
        return self.value == other.value

    @property
    def value(self):
        return self.__value
