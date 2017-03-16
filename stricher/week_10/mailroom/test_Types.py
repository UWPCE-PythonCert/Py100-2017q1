from unittest import TestCase


class TestInfoType(TestCase):
    def test_InfoType(self):
        from Types import InfoType
        info_type = InfoType.DONOR
        self.assertEqual('donor', info_type.value)
        info_type = InfoType.AMOUNT
        self.assertEqual('amount', info_type.value)
