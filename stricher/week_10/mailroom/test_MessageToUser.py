from unittest import TestCase

#TODO: update

# class TestEntryMenu(TestCase):
#
#     def test_get(self):
#
#         from MessageToUser import EntryMenuMessage
#         from TestsData import TestsData
#
#         menu = EntryMenuMessage()
#         self.assertEqual(TestsData.get_menu(), menu.get())


class TestDonationMessageToUser(TestCase):

    def test_get(self):

        from MessageToUser import DonationMessage
        from Types import InfoType

        message = DonationMessage(InfoType.DONOR)
        self.assertEqual(DonationMessage.messages['donor'], message.get())

    def test_get_error(self):

        from MessageToUser import DonationMessage
        from Types import InfoType

        message = DonationMessage(InfoType.DONOR)
        self.assertEqual(DonationMessage.messages['donorError'], message.get_error())
