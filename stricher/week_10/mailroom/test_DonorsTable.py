from unittest import TestCase


class TestDonorsTable(TestCase):

    def test__donor_exists_in_database(self):

        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData
        from PersonId import PersonId
        from Name import PersonName
        from datetime import date

        donors_table = DonorsTable(DonorsDBBenchData().data)
        donor_id = PersonId(PersonName("Ms", "Eliane", "Radigue"), date(1932, 1, 24))
        self.assertEqual(True, donors_table.donor_exists_in_database(donor_id.value))

    def test__get_donors_id(self):
        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData

        bench_data = DonorsDBBenchData().data
        donors_table = DonorsTable(bench_data)
        self.assertEqual(donors_table._get_donors_id(), tuple(bench_data.keys()))

    def test_get_donor(self):
        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData
        from datetime import date
        from Name import PersonName
        from PersonId import PersonId

        bench_data = DonorsDBBenchData().data
        donors_table = DonorsTable(bench_data)
        donor_id = PersonId(PersonName("M", "Jean S", "Bach"), date(1685, 3, 31))
        self.assertEqual(bench_data[donor_id.value], donors_table.get_donor(donor_id.value))

    def test_get_donor_name(self):
        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData
        from datetime import date
        from Name import PersonName
        from PersonId import PersonId

        bench_data = DonorsDBBenchData().data
        donors_table = DonorsTable(bench_data)
        name = PersonName("M", "Jean S", "Bach")
        donor_id = PersonId(PersonName("M", "Jean S", "Bach"), date(1685, 3, 31))
        self.assertEqual(name, donors_table.get_donor(donor_id.value).name)

    def test_get_donors_name(self):
        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData
        from Name import PersonName

        bench_data = DonorsDBBenchData().data
        donors_table = DonorsTable(bench_data)
        donors_names = donors_table.get_donors_names()
        self.assertEqual(6, len(donors_names))
        self.assertEqual(PersonName("M", "Jean S", "Bach"), donors_names[0])
        self.assertEqual(PersonName("Ms", "Eliane", "Radigue"), donors_names[-1])

    def test_add_donor(self):
        from DonorsTable import DonorsTable
        from BenchData import DonorsDBBenchData
        from Name import PersonName
        from Address import Address
        from Donor import Donor
        from PersonId import PersonId
        from datetime import date

        donors_table = DonorsTable(DonorsDBBenchData().data)
        donor_name = PersonName("M", "Ron", "Carter")
        street = "4, place Saint-Sulpice"
        zipcode = "75006"
        city = "Paris"
        country = "France"
        phone = "+33 1 45 43 89 23"
        mail = "ron.carter@thequintet.com"
        donor_address = Address(street=street, zipcode=zipcode, city=city, country=country, phone=phone, mail=mail)
        birth_date = date(1937, 5, 4)
        donor = Donor(name=donor_name, address=donor_address, birth_date=birth_date)
        donors_table.add_donor(donor)
        self.assertEqual(donor, donors_table.get_donor(PersonId(donor_name, birth_date).value))