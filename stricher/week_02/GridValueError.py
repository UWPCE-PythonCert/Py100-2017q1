
class GridValueError(ValueError):
    def __init__(self, message):
        super(ValueError, self).__init__(message)