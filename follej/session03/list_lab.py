#!/usr/bin/env python3
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


def user_add_fruit():
    response = str(input("Add a fruit to the list > "))
    fruit_list.append(response)
    print(fruit_list)


def user_query_fruit():
    line = "Enter a number betwen 1 and " + str(len(fruit_list)) + " > "
    response = int(input(line))
    print("number: {} fruit: {}".format(response, fruit_list[response - 1]))


def add_fruit_beginning(new_fruit):
    global fruit_list
    fruit_list = [new_fruit] + fruit_list
    print(fruit_list)


def insert_fruit_beginning(new_fruit):
    fruit_list.insert(0, new_fruit)
    print(fruit_list)


def display_only_P_fruit():
    for fruit in fruit_list:
        if fruit[0] == 'P':
            print(fruit)


def remove_last_fruit():
    fruit_list.pop()
    print(fruit_list)


def user_delete_fruit():
    global fruit_list
    print(fruit_list)
    line = "Remove fruit from list > "
    response = str(input(line))
    if response in fruit_list:
        while response in fruit_list:
            fruit_list.remove(response)
            print(fruit_list)
    else:
        print(response + " fruit not found")
        user_delete_fruit()


def user_likes_fruit():
    for fruit in fruit_list.copy():
        print(fruit)
        response = ''
        while response != "yes" and response != "no":
            response = input("Do you like {}?  yes/no?".format(fruit.lower()))
        if response == "no":
            fruit_list.remove(fruit)
    print(fruit_list)


def reverse_fruit_list_letter():
    fruit_list_copy = fruit_list.copy()
    for i in range(len(fruit_list_copy)):
        fruit_list_copy[i] = fruit_list_copy[i][::-1]
    fruit_list.pop()
    print(fruit_list + fruit_list_copy)


if __name__ == '__main__':
    user_add_fruit()
    user_query_fruit()
    add_fruit_beginning('Pineapples')
    insert_fruit_beginning('Pomegranates')
    display_only_P_fruit()
    remove_last_fruit()
    fruit_list *= 2
    user_delete_fruit()
    user_likes_fruit()
    reverse_fruit_list_letter()
