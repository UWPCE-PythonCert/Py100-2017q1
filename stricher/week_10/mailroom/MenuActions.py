
class MenuActions:

    from Database import Database
    from io import IOBase

    def __init__(self, donations_db: Database, ostream: IOBase):
        self.__donations_db = donations_db
        self._ostream = ostream

    @property
    def donations_db(self):
        return self.__donations_db
