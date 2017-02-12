# fun with dictionaries
def main():
    dictionary = {
        'Name': 'Chris',
        'City': 'Seattle',
        'Cake': 'Chocolate',
    }
    print('Printing the full dictionary')
    print(dictionary)
    print('')

    print('Removing the Cake')
    dictionary.pop('Cake')
    print(dictionary)
    print('')

    print('Adding the fruit')
    dictionary['Fruit'] = 'Mango'
    print(dictionary)
    print('')

    print('Showing the keys')
    for key in dictionary:
        print(key)
    print('')


    print('Showing the values')
    for value in dictionary.values():
        print(value)
    print('')

    print('Is Cake still a valid key?')
    cakeexist = 'Cake' in dictionary
    print(cakeexist)
    print('')

    print('Is Mango still a valid value?')
    mangoexist = 'Mango' in dictionary.values()
    print(mangoexist)
    print('')

    print('How often is the letter t used in each value?')
    tempdict = {}
    newdict = {}
    dictionary2 = {
        'Name': 'Chris',
        'City': 'Seattle',
        'Cake': 'Chocolate',
    }

    for key in dictionary2:
        count = dictionary2[key].count('t')
        tempdict = {key: count}
        newdict.update(tempdict)
    print(dictionary2)
    print(newdict)
    print('')

    # fun with sets
    s2=set()
    s3=set()
    s4=set()

    for num in range(21):
        if num%2==0:
            s2.update([num])
        if num%3==0:
            s3.update([num])
        if num%4==0:
            s4.update([num])

    print('Display the sets divisible by 2,3 and 4')
    print('S2=',end='',flush=True)
    print(s2)
    print('S3=',end='',flush=True)
    print(s3)
    print('S4=',end='',flush=True)
    print(s4)
    print('')

    print('Does the set S3 exist within the set S2')
    s3ins2 = s3 < s2
    print(s3ins2)
    print('')

    print('Does the set S4 exist within the set S2')
    s4ins2 = s4 < s2
    print(s4ins2)
    print('')

    print('Create a set with the characters \'python\' and then add the character \'i\'')
    pythonset=set('Python')
    pythonset.update('i')
    print(pythonset)
    print('')

    print('Create a frozen set and print it')
    marathonset=frozenset('marathon')
    print(marathonset)
    print('')

    print('Print the union of the python set and the marathon set')
    print(pythonset.union(marathonset))
    print('')

    print('Print the intersection fo the python set and the marathon set')
    print(pythonset.intersection(marathonset))
if __name__ == '__main__':
    main()
