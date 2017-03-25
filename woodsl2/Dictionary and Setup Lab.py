'''
Dictionary and Setup Lab

'''

import sys

dict = {}

# adding value in dictionary
dict['Chris'] = {}
dict['Chris']['Seattle'] = 'Choclate'

# printing dictionary
print 'dictionary = ', dict

# adding fruit and mango in dictionary
dict['fruit'] = 'Mango'

# printing dictionary keys and values
for key, value in dict.items():
    print "key", key
    print "value", value

# check if key 'choclate' exist or not
print 'Choclate' in dict.keys()

# check if value 'Mango' exist or not
print 'Mango' in dict.values()

# creating new dictionary with 't' values
dict2 = {}
for key in dict:
    value = str(dict[key])
    count1 = value.count('t')
    count2 = value.count('T')
    totalcount = count1 + count2
    dict2[key] = totalcount

# creating sets
s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([3, 6, 9, 12, 15, 18])
s4 = set([4, 8, 12, 16, 20])

print s2
print s3
print s4

# check if s3 is subset of s2
print set(s3) < set(s2)

# check if s4 is subset of s2
print set(s4) < set(s2)

# creating python set
python = set(['P', 'y', 't', 'h', 'o', 'n'])
python.add('i')

frozenset = set(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])

# intersection and union of sets
print python.intersection(frozenset)
print python.union(frozenset)