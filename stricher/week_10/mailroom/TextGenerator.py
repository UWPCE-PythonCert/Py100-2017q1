

class TextGenerator:

    def __init__(self):
        self.__str = self._generate()

    def __str__(self):
        return self.__str

    def _generate(self) -> str:
        pass

    from sys import stdout

    def write(self, ostream=stdout) -> None:
        ostream.write(self.__str)
