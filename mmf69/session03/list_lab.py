#!/usr/bin/env python3

'''---------------------------------------------------
List Lab Part 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list.
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
---------------------------------------------------'''

#Create list of fruit
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list, "\n")


#Ask the user for another fruit and add it to the end of the list.
fruit_list.append(input("Please add a fruit to the list:\n"))
print(fruit_list, "\n")

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
try:
    number = int(input("Pick a number:\n"))
    print("The number {} corresponds to {} in the list.\n".format(number, fruit_list[number - 1]))
except IndexError:
    print("That number is not in the list.\n")

#Add another fruit to the beginning of the list using “+” and display the list.
print("Now I will add Pineapple to the front of the list.\n")
fruit_list = ["Pineapple"] + fruit_list
print(fruit_list, "\n")

print("Almost for got Mango")
fruit_list.insert(0, "Mango")
print(fruit_list, "\n")

#Display all the fruits that begin with “P”, using a for loop.
for fruit in fruit_list:
     if fruit[0] == "P":
         print(fruit)
print("\n")

'''-----------------
List Lab Part 2
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete and find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
---------------------'''
print(fruit_list, "\n") #Why is this only printing the fruit entered by the user?


