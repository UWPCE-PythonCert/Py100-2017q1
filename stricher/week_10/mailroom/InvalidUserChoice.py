
class InvalidUserChoice(ValueError):

    def __init__(self, message: str):
        super(InvalidUserChoice, self).__init__(message)