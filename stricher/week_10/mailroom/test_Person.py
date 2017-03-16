from unittest import TestCase


class BenchDataPerson:
    def __init__(self):
        from test_Name import BenchDataName
        from test_Address import BenchDataAddress
        from datetime import date
        from Person import Person

        self.name = BenchDataName().name
        self.address = BenchDataAddress().address
        self.birth_date = date(1952, 5, 23)
        self.person = Person(self.name,
                             self.address,
                             self.birth_date)


class TestPerson(TestCase):

    def test___repr__(self):
        from io import StringIO
        bench = BenchDataPerson()
        ostream = StringIO()
        ostream.write(bench.person.__repr__())
        bench_str = 'Person({},{},{})'.format(bench.name.__repr__(),
                                              bench.address.__repr__(),
                                              bench.birth_date.__repr__())
        self.assertEqual(bench_str, ostream.getvalue())

    def test___str__(self):
        bench = BenchDataPerson()
        bench_str = "{}\n{}".format(bench.name, bench.address)
        self.assertEqual(bench_str, str(bench.person))

    def test__eq__(self):
        self.assertEqual(BenchDataPerson().person, BenchDataPerson().person)