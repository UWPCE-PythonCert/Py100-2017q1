from unittest import TestCase


class TestOrganisationBenchData(TestCase):
    def test_init(self):
        from BenchData import OrganisationBenchData
        from PersonId import PersonId
        from Name import PersonName
        from datetime import date

        music_factory = OrganisationBenchData().data
        cat_anderson = music_factory.get_member(PersonId(name=PersonName("M", "Cat", "Anderson"),
                                                         birth_date=date(1916, 9, 12)))

        bench_str = r"""M Cat Anderson
14, rue Beaune
75007 - Paris
France
+33 1 43 56 78 23
music.factory@drummachine.net
"""
        self.assertEqual(bench_str, str(cat_anderson))

        clifford_brown = music_factory.get_member(PersonId(name=PersonName("M", "Clifford", "Brown"),
                                                           birth_date=date(1930, 10, 30)))
        bench_str = r"""M Clifford Brown
14, rue Beaune
75007 - Paris
France
+33 1 43 56 78 23
music.factory@drummachine.net
"""
        self.assertEqual(bench_str, str(clifford_brown))
