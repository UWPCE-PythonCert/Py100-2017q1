import copy


class SparseArray(object):

    def __init__(self, entries):
        """
        Establishes the empty dict, and then the key counter which preserves the order in which numbers were
        entered into the array.
        """
        self.entries = entries
        self.db = {
            'nonzero': [],
            'zero': []
        }
        self.key_counter = 1
        self.storage_helper(entries)

    def storage_helper(self, entries):
        """Sorts numbers into zero and nonzero integers. Stores only the nonzero in storage.txt."""
        for entry in entries:
            tuple_key = "number_{}".format(self.key_counter)
            if entry == 0:
                self.db['zero'].append((tuple_key, entry))
                self.key_counter += 1
            if entry != 0:
                self.db['nonzero'].append((tuple_key, entry))
                self.key_counter += 1
        storagebuddy = open('storage.txt', 'w')
        storagebuddy.write(str(self.db['nonzero']))

    def __len__(self):
        item_counter = len(self.db['nonzero'])
        item_counter += len(self.db['zero'])
        print("The number of items in my array (including zeros) is: {}".format(item_counter))

    def display_array(self):
        """
        Overwrites the builtin __len__ to smush both zero and nonzero dicts together, and display all numbers in
        their original order.
        :return:
        """
        bucket = []
        bucket += copy.deepcopy(self.db['nonzero'].copy())
        bucket += copy.deepcopy(self.db['zero'].copy())
        bucket.sort(key=lambda tup: tup[0])
        # Apologies to Rick and Mike for using the infamous lambda, I couldn't find any other way to sort by tuple key
        print("Placing nonzero and zero integers back in original order: {}".format(bucket))
        printme = []
        for key, value in bucket:
            printme.append(value)
        print("Full array: {}".format(printme))

    def reset(self, entries):
        self.db = {
            'nonzero': [],
            'zero': []
        }
        self.key_counter = 1
        self.storage_helper(entries)

    def __getitem__(self, index):
        return self.entries[index]

    def __setitem__(self, index, value):
        self.entries[index] = value
        self.reset(self.entries)

    def __delitem__(self, index):
        del self.entries[index]
        self.reset(self.entries)

    def append(self, *additional_numbers):
        additional_numbers = [additional_numbers]
        for number in additional_numbers:
            self.entries.extend(number)
        self.reset(self.entries)


def main():
    len = SparseArray.__len__
    my_array = SparseArray([0, 1, 0, 0, 3, 7])
    len(my_array)
    my_array.display_array()
    print("This class supports indexing, too! The 3rd item is: {}".format(my_array[2]))
    print("And, it supports slicing. The 5th and 6th items are: {}".format(my_array[4:6]))

if __name__ == "__main__":
    main()


