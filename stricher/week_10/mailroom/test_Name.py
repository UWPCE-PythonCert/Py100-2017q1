from unittest import TestCase


class BenchDataName:
    def __init__(self):
        from Name import PersonName
        self.prefix = "M"
        self.first = "Bud"
        self.last = "Powell"
        self.name = PersonName(self.prefix, self.first, self.last)


class TestPersonName(TestCase):
    def test_prefix(self):
        from Name import PersonName
        try:
            name = PersonName("Msss", "Billie", "Holiday")
            self.fail("Should raise ValueError")
        except ValueError as ve:
            bench_str = "InvalidNameError: NameValidation.is_valid_prefix(val: str)" \
                        " - prefix must be either M or Ms"
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

    def test_get_person_name(self):
        from Name import PersonName
        from io import StringIO

        bench_str_ans = "M Miles Davis"
        bench_str_request = "Please enter the person's name [prefix first_name last_name]:"
        ostream = StringIO()
        istream = StringIO(bench_str_ans)
        self.assertEqual(bench_str_ans, str(PersonName.get_from_stream(ostream, istream)))
        self.assertEqual(bench_str_request, ostream.getvalue())

        bench_str_ans = "Mr Miles Davis\nM Miles Davis"
        bench_str_res = "M Miles Davis"
        bench_str_request = "Please enter the person's name [prefix first_name last_name]:" \
                            "Invalid input. Please try again!\n" \
                            "Please enter the person's name [prefix first_name last_name]:"
        ostream = StringIO()
        istream = StringIO(bench_str_ans)
        self.assertEqual(bench_str_res, str(PersonName.get_from_stream(ostream, istream)))
        self.assertEqual(bench_str_request, ostream.getvalue())

        bench_str_ans = "Mr Miles Davis\nMrr Miles Davis\nMrrr Miles Davis"
        bench_str_res = "None"
        bench_str_request = "Please enter the person's name [prefix first_name last_name]:" \
                            "Invalid input. Please try again!\n" \
                            "Please enter the person's name [prefix first_name last_name]:" \
                            "Invalid input. Please try again!\n" \
                            "Please enter the person's name [prefix first_name last_name]:" \
                            "Max number of trials. The program quits!\n"
        ostream = StringIO()
        istream = StringIO(bench_str_ans)
        self.assertEqual(bench_str_res, str(PersonName.get_from_stream(ostream, istream)))
        self.assertEqual(bench_str_request, ostream.getvalue())
