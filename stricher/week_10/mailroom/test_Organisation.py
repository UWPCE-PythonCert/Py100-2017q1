from unittest import TestCase


class TestOrganisation(TestCase):

    def test___repr__(self):
        from Organisation import Organisation
        name = "ALP"
        address = "12, rue de Lille"
        org = Organisation
