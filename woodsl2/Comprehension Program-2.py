import os
import sys

feast = ['lambs', 'sloths', 'orangutans','breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
print comprehension[0]
print comprehension[2]

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals','fruit bats']
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print len(feast)
print len(comp)
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]
print comprehension[0]
print len(comprehension[2])
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print len(comprehension)
print comprehension[0]
comprehension = { x for x in 'aabbbcccc'}
print comprehension

output:

Lambs
Orangutans
5
3
lumberjack
16
6
poached egg and lite spam
set(['a', 'c', 'b'])