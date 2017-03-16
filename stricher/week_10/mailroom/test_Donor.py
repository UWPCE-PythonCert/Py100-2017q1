from unittest import TestCase


class TestDonor(TestCase):
    from Name import Name
    from datetime import date

    @staticmethod
    def __get_donor(donor_name: Name, donation_date: date):
        from BenchData import DonorsDBBenchData
        from DonorId import DonorId
        donors_bench_table = DonorsDBBenchData().data
        return donors_bench_table[DonorId(donor_name, donation_date).value]

    # -- getters

    def test_name(self):
        from Name import Name
        from datetime import date

        donor = self.__get_donor(Name("M", "Charles", "Ives"), date(1874, 10, 20))
        self.assertEqual("Charles", donor.name.first)
        self.assertEqual("Ives", donor.name.last)

        donor = self.__get_donor(Name("M", "Jean S", "Bach"), date(1685, 3, 31))
        self.assertEqual("Jean S", donor.name.first)
        self.assertEqual("Bach", donor.name.last)

    def test_address(self):
        from Address import Address
        from Name import Name
        from datetime import date
        address = Address(street="154, boulevard Saint-Germain", zipcode="75006", city="Paris",
                          country="France", phone="+33 1 45 67 33 12", mail="miles.davis@myself.com")
        donor = self.__get_donor(Name("M", "Miles", "Davis"), date(1926, 5, 26))
        self.assertEqual(address, donor.address)

    def test_birth_date(self):
        from datetime import date
        from Name import Name
        birthdate = date(1931, 12, 2)
        donor = self.__get_donor(Name("M", "Wynton", "Kelly"), date(1931, 12, 2))
        self.assertEqual(birthdate, donor.birth_date)

    def test_id(self):
        from DonorId import DonorId
        from Name import Name
        from datetime import date
        donor_id = DonorId(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        donor = self.__get_donor(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        self.assertEqual(donor_id, donor.id)

    def test___eq__(self):
        from Name import Name
        from datetime import date
        donor = self.__get_donor(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        same_donor = self.__get_donor(Name("M", "Lee", "Morgan"), date(1938, 7, 10))
        self.assertEqual(donor, same_donor)
