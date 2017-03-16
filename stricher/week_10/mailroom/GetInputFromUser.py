
#TODO: complete/update

class GetInputFromUser:

    from Types import InfoType
    from MessageToUser import MessageToUser

    def __init__(self, ostream, istream):
        self.ostream = ostream
        self.istream = istream

    def get_donor_name(self):
        from Types import InfoType
        return self._get_donation(InfoType.DONOR)

    def get_donation_amount(self):
        from Types import InfoType
        return self._get_donation(InfoType.AMOUNT)

    def _request_donation(self, info_type: InfoType):
        from MessageToUser import DonationMessage
        message = DonationMessage(info_type)
        return self._request(message)

    def _validate_donation(self, ans, info_type: InfoType):

        from MessageToUser import DonationMessage
        from Types import InfoType, AnswerType

        if ans.upper() == "M\n" or ans.upper() == "M":
            return "M"
        message = DonationMessage(info_type)
        try:
            float(ans)
            if info_type == InfoType.AMOUNT:
                return float(ans)
            else:
                self.ostream.write(message.get_error())
                return AnswerType.INVALID
        except ValueError as ve:
            if info_type == InfoType.DONOR:
                return ans
            else:
                self.ostream.write(message.get_error())
                return AnswerType.INVALID

    def _get_donation(self, info_type: InfoType):

        from Types import AnswerType

        isInvalid = True
        while isInvalid:
            ans = self._request_donation(info_type)
            ans = self._validate_donation(ans, info_type)
            if ans == AnswerType.INVALID:
                continue
            return ans
