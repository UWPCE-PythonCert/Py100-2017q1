

class Table:

    def __init__(self, table=None):
        if table is not None:
            self._table = table.copy()
        else:
            self._table = dict()

    @property
    def table(self) -> dict:
        return self._table
