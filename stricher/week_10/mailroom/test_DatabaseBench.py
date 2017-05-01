from unittest import TestCase


class TestDatabaseBench(TestCase):

    def test_init(self):
        from BenchData import DatabaseBench

#TODO: check database
        db = DatabaseBench().db
        print("Hello")
