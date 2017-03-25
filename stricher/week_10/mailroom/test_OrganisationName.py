from unittest import TestCase


class TestOrganisationName(TestCase):

    def test_manip(self):

        from Name import OrganisationName

        name = OrganisationName("MusicFactory")
        self.assertEqual('OrganisationName("MusicFactory")', name.__repr__())
        self.assertEqual("MusicFactory", name.__str__())
        self.assertEqual(name, name)

        name2 = OrganisationName("Beats")
        self.assertEqual(False, name == name2)
        self.assertEqual(True, name2 < name)
        self.assertEqual(True, name <= name)
        self.assertEqual(True, name > name2)
        self.assertEqual(False, name2 > name)
        self.assertEqual(True, name > name2)
        self.assertEqual(True, name2 >= name2)

