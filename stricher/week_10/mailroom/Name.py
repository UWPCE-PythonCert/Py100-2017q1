
class Name:

    def __init__(self, prefix: str, first: str, last: str):
        if prefix not in ("M", "Ms"):
            raise ValueError("ValueError: Name(prefix, first, last)"
                             " - prefix must be either M or Ms")
        self.__prefix = prefix
        self.__first = first
        self.__last = last
        self.__full_name = self.__name_builder()

    def __repr__(self):
        return 'Name("{}","{}","{}")'.format(self.prefix, self.first, self.last)

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
