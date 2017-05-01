from unittest import TestCase


class TestOrganisationMember(TestCase):

    def test_init(self):
        from Organisation import Organisation, OrganisationMember
        from Name import PersonName, OrganisationName
        from Address import Address
        from MyDate import MyDate

        address = Address("4, place Saint-Michel", "75006", "Paris", "France",
                          "+33 1 43 57 68 35", "thebeat@soundfactory.com")
        organisation = Organisation(OrganisationName("SoundFactory"), address)
        member = OrganisationMember(PersonName("M", "Nicolas", "Jaar"),
                                    address,
                                    MyDate(1980, 4, 13),
                                    organisation)
        self.assertEqual("M", member.name.prefix)
        self.assertEqual("Nicolas", member.name.first)
        self.assertEqual("Jaar", member.name.last)

    def test_eq(self):
        from Organisation import Organisation, OrganisationMember
        from Name import PersonName, OrganisationName
        from Address import Address
        from MyDate import MyDate

        address = Address("4, place Saint-Michel", "75006", "Paris", "France",
                          "+33 1 43 57 68 35", "thebeat@soundfactory.com")
        organisation = Organisation(OrganisationName("SoundFactory"), address)
        member = OrganisationMember(PersonName("M", "Nicolas", "Jaar"), address,
                                    MyDate(1980, 4, 13), organisation)
        self.assertEqual(member, member)
