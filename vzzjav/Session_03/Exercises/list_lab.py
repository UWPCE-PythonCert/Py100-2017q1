# Javier Vazquez
# Grid Printer
# Jan 29, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/list_lab.html

import os

def main():
    '''List's exercise'''
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    # print(fruits)
    # fruits.append(input("Add fruit: "))
    # print(fruits)
    # print(fruits[int(input("Element to display: "))-1])
    # fruits = [input("Add fruit: ")] + fruits
    # print(fruits)
    # fruits.insert(0, input("Add fruit: "))
    # print(fruits)
    # [print(fruit) for fruit in fruits if "P" in fruit[0]]
    # print(fruits)
    fruitsS1 = fruits[:]
    # del fruits[len(fruits)-1]
    # fruits *= 2
    # print(fruits)
    # fruitRemove = input("Remove fruit: ")
    # [fruits.remove(fruitRemove) for fruit in fruits if fruitRemove in fruits]
    # print(fruits)
    # fruits = fruitsS1[:]
    # print("Fruits serie 1: ", fruits)
    # i = 0
    # removeList = []
    # for fruit in fruits:
    #     while True:
    #         answer = input("Do you like " + fruit + "?")
    #         if answer == "yes":
    #             fruits[i] = fruit.lower()
    #             print(fruits[i])
    #             break
    #         elif answer == "no":
    #             removeList.append(fruit)
    #             break
    #         else:
    #             print("Please just answer [yes] or [no].")
    #             continue
    #     i += 1
    # for fruit in removeList:
    #     fruits.remove(fruit)
    print(fruits)
    fruits = fruitsS1[:]
    print("Fruits serie 1: ", fruits)
    for j in range(len(fruits)):
        fruits[j] = fruits[j][::-1]
    print(fruits)
    del fruitsS1[len(fruitsS1)-1]
    print(fruitsS1)
    print(fruits)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()