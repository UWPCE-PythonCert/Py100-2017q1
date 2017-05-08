
class EmailAddressError(ValueError):
    def __init__(self, message: str):
        super(EmailAddressError, self).__init__(message)


class EmailAddress:

    def __init__(self, address: str):
        from re import compile
        if not bool(compile(r'^[A-Za-z\\.@]*$').search(address)):
            raise EmailAddressError("ValueError: EmailAddress - "
                                    "invalid address format")
        self.__address = address

    @property
    def get(self):
        return self.__address

    def __str__(self):
        return self.get

    def __eq__(self, other):
        return other.get == self.get
