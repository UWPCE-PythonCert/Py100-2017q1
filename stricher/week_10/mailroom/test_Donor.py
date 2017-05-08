from unittest import TestCase


class TestDonor(TestCase):
    from Name import PersonName
    from MyDate import MyDate

    @staticmethod
    def __get_donor(donor_name: PersonName, donation_date: MyDate):
        from BenchData import DonorsDBBenchData
        from PersonId import PersonId
        donors_bench_table = DonorsDBBenchData().data
        return donors_bench_table[PersonId().value]

    # -- getters

    def test_name(self):
        from Name import PersonName
        from MyDate import MyDate

        donor = self.__get_donor(PersonName("M", "Charles", "Ives"), MyDate(1874, 10, 20))
        self.assertEqual("Charles", donor.name.first)
        self.assertEqual("Ives", donor.name.last)

        donor = self.__get_donor(PersonName("M", "Jean S", "Bach"), MyDate(1685, 3, 31))
        self.assertEqual("Jean S", donor.name.first)
        self.assertEqual("Bach", donor.name.last)

    def test_address(self):
        from Address import Address
        from Name import PersonName
        from MyDate import MyDate
        address = Address(street="154, boulevard Saint-Germain", zipcode="75006", city="Paris",
                          country="France", phone="+33 1 45 67 33 12", mail="miles.davis@myself.com")
        donor = self.__get_donor(PersonName("M", "Miles", "Davis"), MyDate(1926, 5, 26))
        self.assertEqual(address, donor.address)

    def test_birth_date(self):
        from MyDate import MyDate
        from Name import PersonName
        birthdate = MyDate(1931, 12, 2)
        donor = self.__get_donor(PersonName("M", "Wynton", "Kelly"), MyDate(1931, 12, 2))
        self.assertEqual(birthdate, donor.birth_date)

    def test_id(self):
        from PersonId import PersonId
        from Name import PersonName
        from MyDate import MyDate
        donor_id = PersonId()
        donor = self.__get_donor(PersonName("M", "Lee", "Morgan"), MyDate(1938, 7, 10))
        self.assertEqual(donor_id, donor.id)

    def test___eq__(self):
        from Name import PersonName
        from MyDate import MyDate
        donor = self.__get_donor(PersonName("M", "Lee", "Morgan"), MyDate(1938, 7, 10))
        same_donor = self.__get_donor(PersonName("M", "Lee", "Morgan"), MyDate(1938, 7, 10))
        self.assertEqual(donor, same_donor)
