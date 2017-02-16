#!/usr/bin/env python3

__author__ = 'raudel'


def main():

    fruits_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    print('This is the list of all fruits', fruits_list)

    new_fruit = input('Please, enter a new fruit:')

    fruits_list.append(new_fruit)

    print('This is the list of all fruits', fruits_list)

    fruit_index = input('Please, enter the fruit index you want to display:')

    print('This is the fruit with index ' + fruit_index + ' in your list of fruits', fruits_list[int(fruit_index)-1])

    my_fruit = ['Mango']

    result_list = my_fruit + fruits_list

    print(result_list)

    my_fruit = 'Banana'

    fruits_list.insert(0, my_fruit)

    print(fruits_list)

    for i in fruits_list:
        if i[0] == 'P': print('Fruits starting with P: ', i)


if __name__ == '__main__':
    main()