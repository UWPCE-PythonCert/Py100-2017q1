from unittest import TestCase


class BenchDataAddress:
    def __init__(self):
        from Address import Address
        from EmailAddress import EmailAddress
        self.street = "15, rue de Lille"
        self.zipcode = "75007"
        self.city = "Paris"
        self.country = "France"
        self.phone = "+33 1 42 45 56 67"
        self.mail = EmailAddress("nobody@nowhere.com")
        self.address = Address(self.street, self.zipcode, self.city, self.country, self.phone, self.mail)


class TestAddress(TestCase):
    def test___repr__(self):
        from io import StringIO
        bench = BenchDataAddress()
        ostream = StringIO()
        ostream.write(bench.address.__repr__())
        bench_str = 'Address("{}","{}","{}","{}","{}","{}")'.format(bench.street,
                                                                    bench.zipcode,
                                                                    bench.city,
                                                                    bench.country,
                                                                    bench.phone,
                                                                    bench.mail.get)
        self.assertEqual(bench_str, ostream.getvalue())

    def test___str__(self):
        bench = BenchDataAddress()
        bench_str = "{}\n{} - {}\n{}\n{}\n{}\n".format(bench.street,
                                                       bench.zipcode,
                                                       bench.city,
                                                       bench.country,
                                                       bench.phone,
                                                       str(bench.mail))
        self.assertEqual(bench_str, str(bench.address))

    def test___eq__(self):
        self.assertEqual(BenchDataAddress().address, BenchDataAddress().address)
