
from Table import Table


class PersonTable(Table):

    from Person import Person
    from Name import PersonName

    def __init__(self, table=None):
        super(PersonTable, self).__init__(table)

    def person_exists_in_database(self, person_id: str) -> bool:
        return person_id in self.table

    def _get_person_id(self) -> tuple:
        return tuple(self.table.keys())

    def get_person(self, person_id: str) -> Person:
        if self.person_exists_in_database(person_id):
            return self.table[person_id]
        raise ValueError("ValueError: get_person(person_id): - "
                         "person does not exist in the database")

    def get_person_name(self, person_id: str) -> PersonName:
        return self.get_person(person_id).name

    def get_persons_names(self) -> list:
        donors = [person.name for person in self._table.values()]
        donors.sort()
        return donors

    def add_person(self, person: Person) -> None:
        self.table[person.id.value] = person