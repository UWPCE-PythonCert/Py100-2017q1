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
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit, "\n")


#Ask the user for another fruit and add it to the end of the list.
fruit.append(input("Pleaae add a fruit to the list:\n"))
print(fruit, "\n")

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
while True:
    try:
        number = int(input("Pick a number:\n"))
        print("The number {} corresponds to {} in the list.\n".format(number,fruit[number - 1]))
    except IndexError:
        print("That number is not in the list")
