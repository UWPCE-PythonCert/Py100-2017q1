import collections


class SparseArray(collections.MutableSequence):
    def __init__(self, iterable):
        self.items = dicts = {}
        self._length = 0
        for i, value in enumerate(iterable):
            self._length += 1
            if value != 0:
                dicts.update({i: value})

    def print_dicts(self):
        return self.items.items()

    def __str__(self):
        string = ["["]
        for i in range(len(self)):
            string.append("{}".format(self.items.get(i, 0)))
            string.append(", ")
        string[-1] = "]"
        return "".join(string)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.__str__())

    def __iter__(self):
        pass

    def __len__(self):
        return self._length

    def __delitem__(self, key):
        # TODO - this one.  Have to update the key dict values... someday.
        pass

    def __getitem__(self, key):
        if isinstance(key, slice):
            if key.stop is not None:
                if key.stop > len(self):
                    raise IndexError
            indices = key.indices(len(self))
            return [self.items.get(k, 0) for k in range(*indices)]
        else:
            if key >= self.__len__():
                raise IndexError
            return self.items.get(key, 0)

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            if key.stop is not None:
                if key.stop > len(self):
                    raise IndexError

            indices = key.indices(len(self))
            j = 0
            for k in range(*indices):
                if k in self.items and value[j] == 0:
                    del self.items[k]
                elif value[j] == 0:
                    pass
                else:
                    self.items[k] = value[j]
                j += 1

        else:
            if key >= self.__len__():
                raise IndexError
            if key in self.items and value == 0:
                del self.items[key]
            elif value == 0:
                pass
            else:
                self.items[key] = value

    def insert(self, index, value):
        pass

    def append(self, value):
        key = self._length
        self._length += 1
        if value == 0:
            pass
        else:
            self.items.update({key: value})
