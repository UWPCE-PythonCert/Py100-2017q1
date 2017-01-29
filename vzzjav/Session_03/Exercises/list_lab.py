# Javier Vazquez
# Grid Printer
# Jan 29, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/list_lab.html

import os

def createList():
    '''Create a list'''
    return ["Apples", "Pears", "Oranges", "Peaches"]



def main():
    '''List's exercise'''
    fruits = createList()
    print(fruits)
    fruits.append(input("Add fruit: "))
    print(fruits)
    print(fruits[int(input("Element to display: "))-1])
    fruits = [input("Add fruit: ")] + fruits
    print(fruits)
    fruits.insert(0, input("Add fruit: "))
    print(fruits)
    [print(fruit) for fruit in fruits if "P" in fruit[0]]

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()