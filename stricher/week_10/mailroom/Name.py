class InvalidNameError(ValueError):
    def __init__(self, message: str):
        super(InvalidNameError, self).__init__(message)


class Name:
    def name(self) -> str:
        pass

    def __str__(self) -> str:
        return "{}".format(self.name)

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def __le__(self, other) -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other) -> bool:
        return not self.__le__(other)

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)


class PersonName(Name):
    from io import IOBase

    def __init__(self, prefix: str, first: str, last: str):
        super(PersonName, self).__init__()
        self.__prefix = PersonName.validate_prefix(prefix)
        self.__first = PersonName.validate_name_component(first)
        self.__last = PersonName.validate_name_component(last)
        self.__full_name = self.__name_builder()

    @staticmethod
    def validate_prefix(val: str) -> str:
        if val in ("M", "Ms"):
            return val
        raise InvalidNameError("InvalidNameError: "
                               "NameValidation.is_valid_prefix(val: str)"
                               " - prefix must be either M or Ms")

    @staticmethod
    def validate_name_component(val: str) -> str:
        from re import compile
        if len(val) >= 2 and bool(compile(r'^[A-Za-z -]*$').search(val)):
            return val
        raise InvalidNameError('InvalidNameError: NameValidation.is_valid_name_component(val)'
                               ' - "val" must contain at least two characters '
                               'and characters must be in the range [A-Za-z]')

    def __name_builder(self) -> str:
        return self.first + " " + self.last

    def __repr__(self):
        return 'PersonName("{}","{}","{}")'.format(self.prefix, self.first, self.last)

    def __lt__(self, other):
        return self.last < other.last

    def __le__(self, other):
        return self.__lt__(other) or self.last == other.last

    @property
    def prefix(self):
        return self.__prefix

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def full_name(self) -> str:
        return self.__full_name

    @property
    def name(self) -> str:
        return self.prefix + " " + self.full_name

    @classmethod
    def from_string(cls, name: str):
        splitted = name.split(" ")
        if len(splitted) != 3:
            error_message = 'InvalidNameError: PersonName.get_from_string(name: str).' \
                            ' String must be formatted as "prefix first_name last_name"'
            raise InvalidNameError(error_message)
        return cls(splitted[0], splitted[1], splitted[2])

    @staticmethod
    def get_from_stream(ostream: IOBase, istream: IOBase, message=None, max_attempt_message=None, max_trials=3):
        from Utilities import Utilities
        if message is None:
            message = "Please enter the person's name [prefix first_name last_name]:"

        error_message = "Invalid input. Please try again!\n"
        trials_counter = 1
        while trials_counter <= max_trials:
            user_input = Utilities.request(ostream, istream, message)
            try:
                splitted = user_input.split(" ")
                if len(splitted) != 3:
                    raise InvalidNameError(error_message)
                prefix = PersonName.validate_prefix(splitted[0])
                first_name = PersonName.validate_name_component(splitted[1])
                last_name = PersonName.validate_name_component(splitted[2])
                return PersonName(prefix, first_name, last_name)
            except InvalidNameError:
                if trials_counter == max_trials:
                    break
                ostream.write(error_message)
                trials_counter += 1
        if max_attempt_message is None:
            max_attempt_message = "Max number of trials. The program quits!\n"
        ostream.write(max_attempt_message)


class OrganisationName(Name):
    def __init__(self, name: str):
        super(OrganisationName, self).__init__()
        self.__name = name

    def __repr__(self):
        return 'OrganisationName("{}")'.format(self.name)

    @property
    def name(self):
        return self.__name
