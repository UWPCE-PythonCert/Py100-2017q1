
from EmailAddress import EmailAddress


class Address:

    def __init__(self, street: str, zipcode: str, city: str,
                 country: str, phone: str, mail: EmailAddress):
        self.__street = street
        self.__zipcode = zipcode
        self.__city = city
        self.__country = country
        self.__phone = phone
        self.__mail = mail

    def __repr__(self):
        return 'Address("{}","{}","{}","{}","{}","{}")'.\
            format(self.street, self.zipcode,
                   self.city, self.country,
                   self.phone, self.mail)

    def __str__(self):
        return self.street + "\n" \
               + self.zipcode + " - " \
               + self.city + "\n" \
               + self.country + "\n" \
               + self.phone + "\n" \
               + str(self.mail) + "\n"

    def __eq__(self, other):
        return self.street == other.street \
               and self.zipcode == other.zipcode \
               and self.city == other.city \
               and self.country == other.country \
               and self.phone == other.phone \
               and self.mail == other.mail

    @property
    def street(self) -> str:
        return self.__street

    @property
    def zipcode(self) -> str:
        return self.__zipcode

    @property
    def city(self) -> str:
        return self.__city

    @property
    def country(self) -> str:
        return self.__country

    @property
    def phone(self) -> str:
        return self.__phone

    from EmailAddress import EmailAddress

    @property
    def mail(self) -> EmailAddress:
        return self.__mail
