
class InvalidInput(ValueError):

    def __init__(self, message: str):
        super(InvalidInput, self).__init__(message)