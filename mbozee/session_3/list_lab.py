#!/usr/bin/env python3

# Session 3: List Lab

# Series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

fruits.append(input('Give me another fruit > '))
print(fruits)

number = int(input('Give me a number > '))
print(number, fruits[number-1])

fruits = list('Mangoes') + fruits
print(fruits)

fruits.insert(0, 'Cherries')
print(fruits)

for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)


# Series 2