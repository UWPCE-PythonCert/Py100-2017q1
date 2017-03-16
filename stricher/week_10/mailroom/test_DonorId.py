from unittest import TestCase


class TestDonorId(TestCase):

    def test_equality(self):
        from DonorId import DonorId
        from datetime import date
        from Name import Name

        donor1 = DonorId(Name("M", "Miles", "Davis"), date(1926, 5, 26))
        donor2 = DonorId(Name("M", "Miles", "Davis"), date(1926, 5, 26))
        self.assertEqual(donor1, donor2)