from unittest import TestCase


class BenchDataName:

    def __init__(self):
        from Name import PersonName
        self.prefix = "M"
        self.first = "Bud"
        self.last = "Powell"
        self.name = PersonName(self.prefix, self.first, self.last)


class TestName(TestCase):

    def test_prefix(self):
        from Name import PersonName
        try:
            name = PersonName("Msss", "Billie", "Holiday")
            self.fail("Should raise ValueError")
        except ValueError as ve:
            bench_str = "ValueError: PersonName(prefix, first, last) - prefix must be either M or Ms"
            self.assertEqual(bench_str, str(ve))

    def test___repr__(self):
        bench = BenchDataName()
        from io import StringIO
        ostream = StringIO()
        ostream.write(bench.name.__repr__())
        bench_str = 'PersonName("{}","{}","{}")'.format(bench.prefix, bench.first, bench.last)
        self.assertEqual(bench_str, ostream.getvalue())

    def test___str__(self):
        bench = BenchDataName()
        bench_str = "{} {} {}".format(bench.prefix, bench.first, bench.last)
        self.assertEqual(bench_str, str(bench.name))

    def test___eq__(self):
        return self.assertEqual(BenchDataName().name, BenchDataName().name)

    def test___lt__(self):
        from Name import PersonName
        powell = PersonName("M", "Bud", "Powell")
        radigue = PersonName("Ms", "Eliane", "Radigue")
        self.assertEqual(True, powell < radigue)

        bach = PersonName("M", "Jean S", "Bach")

        names = [radigue, bach, powell]
        names.sort()
        self.assertEqual(bach, names[0])
        self.assertEqual(powell, names[1])
        self.assertEqual(radigue, names[-1])