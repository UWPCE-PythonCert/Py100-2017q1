class DatabaseError(ValueError):

    def __init__(self, message: str):
        super(DatabaseError, self).\
            __init__("DatabaseError: {}".format(message))