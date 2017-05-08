from unittest import TestCase


class TestEmailAddress(TestCase):

    def test_get(self):
        from EmailAddress import EmailAddress
        mail = EmailAddress("nobody@nowhere.com")
        self.assertEqual("nobody@nowhere.com", mail.get)

    def test_str(self):
        from EmailAddress import EmailAddress
        mail = EmailAddress("foo@bar.com")
        self.assertEqual("foo@bar.com", str(mail))
