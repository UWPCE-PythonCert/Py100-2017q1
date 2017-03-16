

class Organisation:

    def __init__(self, name: str):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def __repr__(self):
        return "Organisation({},{},{})".format(self.name, self.address, self.phone)

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

