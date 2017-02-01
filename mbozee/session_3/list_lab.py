#!/usr/bin/env python3

# Session 3: List Lab

# Series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

fruits.append(input('Give me another fruit > '))
print(fruits)

# number = int(input('Give me a number > '))
# print(number, fruits[number-1])

# fruits = list('Mangoes') + fruits
# print(fruits)

fruits.insert(0, 'Cherries')
print(fruits)

for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)


# Series 2

# print(fruits)
#
# fruits.pop()
# print(fruits)
#
# fruit_delete = input('Give me a fruit to delete > ')
# fruits.remove(fruit_delete)
# print(fruits)
#
# fruits = fruits * 2
# print(fruits)
#
# while fruits:
#     fruits.remove(input('Give me a fruit to delete >'))
#     print(fruits)


# Series 3

# print(fruits)
#
# fruits_to_remove = []
# for fruit in fruits:
#     response = input('Do you like ' + fruit.lower() + '? (yes/no)')
#     if response == 'no'.lower():
#         fruits_to_remove.append(fruit)
#         print(fruit)
#     elif response == 'yes'.lower():
#         print('Me too!')
# print(fruits_to_remove)
# for fruit in fruits_to_remove:
#     fruits.remove(fruit)
# print(fruits)


# Series 4

new_fruits = fruits[:]
for fruit in new_fruits:
    fruit = fruit[::-1] # doesn't work
print('New fruits reversed:')
print(new_fruits) # incorrect: not reversed

fruits.pop()
print(fruits)
print(new_fruits)