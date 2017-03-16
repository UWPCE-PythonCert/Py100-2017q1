
class Utilities:

    @staticmethod
    def get_unique_items(container: tuple) -> tuple:
        if type(container) != tuple:
            raise TypeError("get_unique_items(container: tuple) - container must be of tuple type")
        if len(container) == 1:
            return tuple(container)
        ans = []
        for item in container:
            if item not in ans:
                ans.append(item)
        return tuple(ans)

    @staticmethod
    def request(ostream, istream, message: str) -> str:
        numChars = ostream.write(message)
        ostream.flush()
        input = istream.readline().rstrip()
        istream.flush()
        return input