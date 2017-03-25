from unittest import TestCase


class TestOrganisationMember(TestCase):

    def test_init(self):
        from Organisation import Organisation, OrganisationMember
        from Name import PersonName
        organisation = Organisation()
        member = OrganisationMember(PersonName("M", "Nicolas", "Jaar"))
        self.assertEqual("M", member.name.prefix)
        self.assertEqual("Nicolas", member.name.first)
        self.assertEqual("Jaar", member.name.last)

    def test_eq(self):
        from Organisation import OrganisationMember
        from Name import PersonName
        member = OrganisationMember(PersonName("M", "Nicolas", "Jaar"))
        self.assertEqual(member, member)
