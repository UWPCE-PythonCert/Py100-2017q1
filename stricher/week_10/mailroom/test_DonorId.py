from unittest import TestCase


class TestDonorId(TestCase):

    def test_equality(self):
        from PersonId import PersonId
        from datetime import date
        from Name import PersonName

        donor1 = PersonId(PersonName("M", "Miles", "Davis"), date(1926, 5, 26))
        donor2 = PersonId(PersonName("M", "Miles", "Davis"), date(1926, 5, 26))
        self.assertEqual(donor1, donor2)