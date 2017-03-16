#TODO: update

# from unittest import TestCase
#
#
# class TestGetInputFromUser(TestCase):
#
#     from Types import InfoType
#
#     def test__request_donation(self):
#
#         from Types import InfoType
#
#         def __test_helper(name: str, info_type: InfoType) -> None:
#
#             from GetInputFromUser import GetInputFromUser
#             from MessageToUser import DonationMessage
#             from io import StringIO
#
#             ostream = StringIO()
#             istream = StringIO(name)
#             user_input = GetInputFromUser(ostream, istream)
#             self.assertEqual(name, user_input._request_donation(info_type))
#             message = DonationMessage(info_type)
#             self.assertEqual(message.get(), ostream.getvalue())
#
#         name = "Jean S Bach"
#         __test_helper(name, InfoType.DONOR)
#
#         name = "34534"
#         __test_helper(name, InfoType.AMOUNT)
#
#         name = "M"
#         __test_helper(name, InfoType.DONOR)
#
#     def test__validate_donation(self):
#
#         from Types import InfoType
#
#         def __test_helper(name: str, info_type: InfoType,
#                           error=False) -> None:
#
#             from MessageToUser import DonationMessage
#             from GetInputFromUser import GetInputFromUser
#             from Types import AnswerType
#             from io import StringIO
#
#             ostream = StringIO()
#             istream = StringIO(name)
#             user_input = GetInputFromUser(ostream, istream)
#             ans = user_input._request_donation(info_type)
#             message = DonationMessage(info_type)
#
#             if not error:
#                 self.assertEqual(name, user_input._validate_donation(ans, info_type))
#                 self.assertEqual(message.get(), ostream.getvalue())
#             else:
#                 self.assertEqual(AnswerType.INVALID,
#                                  user_input._validate_donation(ans, info_type))
#                 benchStr = message.get() + message.get_error()
#                 self.assertEqual(benchStr, ostream.getvalue())
#
#         name = "Jean S Bach"
#         __test_helper(name, InfoType.DONOR)
#
#         name = "456456"
#         __test_helper(name, InfoType.DONOR, error=True)
#
#     def test__get_donation(self):
#
#         from Types import InfoType
#
#         def __test_helper(var: str, info_type: InfoType):
#
#             from GetInputFromUser import GetInputFromUser
#             from MessageToUser import DonationMessage
#             from io import StringIO
#
#             istream = StringIO(var)
#             ostream = StringIO()
#             user_input = GetInputFromUser(ostream, istream)
#             if var == 'm':
#                 var = 'M'
#             if info_type.value == InfoType.AMOUNT.value and var != 'M':
#                 var = float(var)
#             self.assertEqual(var, user_input._get_donation(info_type))
#             message = DonationMessage(info_type)
#             self.assertEqual(message.get(), ostream.getvalue())
#
#         __test_helper("Charles Ives", InfoType.DONOR)
#         __test_helper("Lee Morgan", InfoType.DONOR)
#         __test_helper("m", InfoType.DONOR)
#         __test_helper("M", InfoType.DONOR)
#         __test_helper("3456.67", InfoType.AMOUNT)
#         __test_helper("m", InfoType.AMOUNT)
#         __test_helper("M", InfoType.AMOUNT)
#
#     def __test_get_donor_amount_helper(self, val: str, info_type: InfoType):
#
#         from io import StringIO
#         from MessageToUser import DonationMessage
#         from GetInputFromUser import GetInputFromUser
#         from Types import InfoType
#
#         ostream = StringIO()
#         istream = StringIO(val)
#         user_input = GetInputFromUser(ostream, istream)
#         if info_type == InfoType.DONOR:
#             user_input.get_donor_name()
#         else:
#             user_input.get_donation_amount()
#         message = DonationMessage(info_type)
#         self.assertEqual(message.get(), ostream.getvalue())
#
#     def test_get_donor_name(self):
#         from Types import InfoType
#         val = "Miles Davis"
#         info_type = InfoType.DONOR
#         self.__test_get_donor_amount_helper(val, info_type)
#
#     def test_get_donation_amount(self):
#         from Types import InfoType
#         val = "456.67"
#         info_type = InfoType.AMOUNT
#         self.__test_get_donor_amount_helper(val, info_type)
#
#     def test__request_entry_menu(self):
#
#         from io import StringIO
#         from GetInputFromUser import GetInputFromUser
#         from TestsData import TestsData
#
#         ostream = StringIO()
#         istream = StringIO("1")
#         user_input = GetInputFromUser(ostream, istream)
#         ans = user_input._print_menu_and_request_user_choice()
#         self.assertEqual("1", ans)
#         self.assertEqual(TestsData.get_menu_string(), ostream.getvalue())
#
#     def test__validate_entry_menu(self):
#
#         from io import StringIO
#         from GetInputFromUser import GetInputFromUser
#
#         ostream = StringIO()
#         istream = StringIO("1")
#         user_input = GetInputFromUser(ostream, istream)
#         ans = user_input._print_menu_and_request_user_choice()
#         ans = user_input._validate_user_choice(ans)
#         self.assertEqual("1", ans)
#
#     def test_get_action_from_user(self):
#
#         from io import StringIO
#         from GetInputFromUser import GetInputFromUser
#
#         ostream = StringIO()
#         istream = StringIO("1")
#
#         user_input = GetInputFromUser(ostream, istream)
#         self.assertEqual("1", user_input._get_action_from_user())
