from unittest import TestCase


class TestOrganisationBenchData(TestCase):
    def test_init(self):
        from BenchData import OrganisationBenchData
        from PersonId import PersonId

        music_factory = OrganisationBenchData().data
        cat_anderson = music_factory.get_member(PersonId().value)

        bench_str = r"""M Cat Anderson
14, rue Beaune
75007 - Paris
France
+33 1 43 56 78 23
music.factory@drummachine.net
"""
        self.assertEqual(bench_str, str(cat_anderson))

        clifford_brown = music_factory.get_member(PersonId().value)
        bench_str = r"""M Clifford Brown
14, rue Beaune
75007 - Paris
France
+33 1 43 56 78 23
music.factory@drummachine.net
"""
        self.assertEqual(bench_str, str(clifford_brown))
