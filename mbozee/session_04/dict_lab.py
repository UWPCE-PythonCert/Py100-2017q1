#!/usr/bin/env python3

# Session 4: Dictionary and Set Lab

################
# DICTIONARIES #
################
print('------DICTIONARIES------')

dict1 = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}

# Display the dictionary
print(dict1)

# Delete the entry for 'cake'
dict1.pop('cake')
print(dict1)

# Add an entry for 'fruit'
dict1['fruit'] = 'Mango'
print(dict1)

# Display the dictionary keys
for keys in dict1:
    print(keys, end=', ')
print('\n', end='')

# Display the dictionary values
for values in dict1:
    print(values, end=", ")
print('\n', end='')

# Display whether 'cake' is a key in the dictionary
if 'cake' in dict1.keys():
    print(True)
else:
    print(False)

# Display whether 'Mango' is a value in the dictionary
if 'Mango' in dict1.values():
    print(True)
else:
    print(False)

# Make a dictionary using the same keys but with the number of t's in each value as the value
print(dict1)
for keys, values in dict1.items():
    new_value = values.lower().count('t')
    dict1[keys] = new_value
print(dict1)

########
# SETS #
########
print('------SETS------')

s2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
s3 = {3, 6, 9, 12, 15, 18}
s4 = {4, 8, 12, 16, 20}

# Display the sets
print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2
# Display if s4 is a subset of s2
def subset_check(set_to_check):
    """Print whether set is subset of s2."""
    if set_to_check.issubset(s2):
        print(True)
    else:
        print(False)

subset_check(s3)
subset_check(s4)

# Create a set with the letters in 'Python'
set_python = set('Python')
print(set_python)

# Add 'i' to set_python
set_python.add('i')
print(set_python)

# Create a frozenset with the letters in 'marathon'
fs_marathon = frozenset('marathon')
print(fs_marathon)

# Display the union and intersection of set_python and fs_marathon
print(set_python.union(fs_marathon)) # union
print(set_python.intersection(fs_marathon)) # intersection
