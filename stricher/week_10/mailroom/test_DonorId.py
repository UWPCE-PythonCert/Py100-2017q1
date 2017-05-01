from unittest import TestCase


class TestDonorId(TestCase):

    def test_equality(self):
        from PersonId import PersonId
        from MyDate import MyDate
        from Name import PersonName

        donor1 = PersonId()
        donor2 = PersonId()
        self.assertEqual(donor1, donor2)