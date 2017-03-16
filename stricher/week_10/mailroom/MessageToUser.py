from Types import InfoType

# TODO: complete/updae, write a class hierarchie


class MessageToUser:
    pass

    def get(self):
        pass

    def get_error(self):
        pass

class DonationMessage(MessageToUser):

    messages = dict(donor="Please enter the donor's full name - [M] to get back to the menu: ",
                    amount="Please enter the donation amount - [M] to get back to the menu: ",
                    donorError="Invalid input. Please enter a name, not a value. Try again.\n",
                    amountError="Invalid input. Please enter a numeric value. Try again.\n")

    def __init__(self, info_type: InfoType):
        self.info_type = info_type

    def get(self):
        return self.messages[self.info_type.value]

    def get_error(self):
        return self.messages[self.info_type.value + 'Error']
