from MenuActions import MenuActions


class QuitMenuActions(MenuActions):

    from Database import Database, DBWriterType
    from io import IOBase

    def __init__(self, donations_db: Database, ostream: IOBase):
        super(QuitMenuActions, self).__init__(donations_db, ostream)

    def _save_database(self, writer_type: DBWriterType) -> None:
        self._ostream.write("Writing the database to a"
                             " {} database".format(writer_type.name))
        self.donations_db.write(writer_type)
        self.quit_program()

    def save_database_sql_lite(self) -> None:
        from Database import DBWriterType
        self._save_database(DBWriterType.sql_lite)

    def save_database_sql_server(self) -> None:
        from Database import DBWriterType
        self._save_database(DBWriterType.sql_server)

    def quit_program(self) -> None:
        self._ostream.write("The program quits. Goodbye !")
        from sys import exit
        exit(0)
