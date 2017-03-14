import collections


class SparseArray(collections.MutableSequence):
    def __init__(self, iterable):
        self.items = dicts = {}
        self.length = 0
        for i, value in enumerate(iterable):
            if value != 0:
                dicts.update({i: value})
            self.length += 1

    def __str__(self):
        string = ["["]
        for i in range(self.__len__()):
            string.append("{}".format(self.items.get(i, 0)))
            string.append(", ")
        string[-1] = "]"
        return "".join(string)

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        return self.length

    def __delitem__(self, key):
        pass

    def __getitem__(self, item):
        if item >= self.__len__():
            raise IndexError
        return self.items.get(item, 0)

    def __setitem__(self, key, value):
        if key >= self.__len__():
            raise IndexError
        elif key in self.items and value == 0:
            del self.items[key]
        elif value == 0:
            pass
        else:
            self.items[key] = value

    def insert(self, index, value):
        pass

    def append(self, value):
        key = self.length
        self.length += 1
        if value == 0:
            pass
        else:
            self.items.update({key: value})


sa = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0])
print(sa)
print(len(sa))
print(sa[9])
sa[2] = 5
print(sa[2])
print(sa[1])
sa[1] = 0
print(sa[1])
sa[3] = 0
print(sa[1])
print(sa)
sa.append(5)
print(sa)
