

class Name:
    pass


class PersonName(Name):

    def __init__(self, prefix: str, first: str, last: str):
        if prefix not in ("M", "Ms"):
            raise ValueError("ValueError: PersonName(prefix, first, last)"
                             " - prefix must be either M or Ms")
        self.__prefix = prefix
        self.__first = first
        self.__last = last
        self.__full_name = self.__name_builder()

    def __repr__(self):
        return 'PersonName("{}","{}","{}")'.format(self.prefix, self.first, self.last)

    def __str__(self):
        return "{} {} {}".format(self.prefix, self.first, self.last)

    def __eq__(self, other):
        return self.prefix == other.prefix \
               and self.first == other.first \
               and self.last == other.last

    def __lt__(self, other):
        return self.last < other.last

    def __name_builder(self) -> str:
        return self.first + " " + self.last

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


class OrganisationName(Name):

    def __init__(self, name: str):
        self.__name = name

    def __repr__(self):
        return 'OrganisationName("{}")'.format(self.name)

    def __str__(self):
        return "{}".format(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    @property
    def name(self):
        return self.__name
