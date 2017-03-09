__author__ = 'raudel'


def main():
    my_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

    dict2 = my_dict.copy()



    print(my_dict)

    del my_dict['cake']

    print('Deleting entry for cake..', my_dict)

    my_dict['fruit'] = 'Mango'

    print('Adding entry fruit with value of Mango..', my_dict)

    # Display the dictionary keys.

    print('Display the dictionary keys...', list(my_dict.keys()))

    # Display whether or not “cake” is a key in the dictionary

    flag = 'cake' in my_dict.keys()
    print('It is ', flag, ' that cake is a key of the dictionary..')

    # Display whether or not “Mango” is a value in the dictionary (i.e. True).

    flag = 'Mango' in my_dict.values()

    print('It is ', flag, ' that Mango is a value in the dictionary..')

    # Make a dictionary using the same keys but with the number of ‘t’s in each value as the value.

    temp_dict = {}
    for i in dict2.keys():
        value = dict2[i]
        temp_dict[i] = value.count('t')

    print(temp_dict)

    # Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(0, 20):
        if i*2 <= 20:
            s2.add(i*2)
        if i*3 <= 20:
            s3.add(i*3)
        if i*4 <= 20:
            s4.add(i*4)

    print(s2, s3, s4)

    print(s3.issubset(s2))
    print(s4.issubset(s2))

    # Create a set with the letters in ‘Python’ and add ‘i’ to the set

    my_set = set('Python')

    my_set.add('i')

    print(my_set)

    # Create a frozenset with the letters in ‘marathon’

    my_fro_set = frozenset('marathon')

    print(my_fro_set)

    # display the union and intersection of the two sets.

    my_union = my_set.union(my_fro_set)

    print('This is the union of these two sets:', my_union)

    my_intersection = my_set.intersection(my_fro_set)

    print('This is the intersection of these two sets:', my_intersection)



if __name__ == '__main__':
    main()