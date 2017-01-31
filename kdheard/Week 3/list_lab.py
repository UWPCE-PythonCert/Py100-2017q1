#!/usr/bin/env python3

import string
import copy
s = string
'''
TODO Input validation.  while True
"break" to break out of while loop

'''

def main():

    print("--SERIES 1--")
    border = "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("These are the current fruits we have: " + str(fruits) + "\n")
    response1 = input("What is your favorite fruit? ")
    fruits.append(response1)
    print("Thanks! We added it to our fruits: " + str(fruits) + "\n")
    try:
        response2 = input("Give me a number from 0 - 4: ")
        print("This was your number: " + str(response2))
        print("This is the fruit in the list that it responds to: " + fruits[int(response2)] + "\n")
    except:
        print('Invalid input. We will start over.')
        main()

    fruits = ["Watermelon"] + fruits
    print("I added Watermelon: " + str(fruits) + "\n")
    fruits.insert(0,"Persimmons")
    print("I added Persimmons too: " + str(fruits) + "\n")

    [print(item) for item in fruits if item.startswith('P')]
    print(border)


    print("--SERIES 2-- \nHere are the fruits we have now: " + str(fruits) + "\n")
    splat = fruits[-1]
    fruits.remove(splat)
    print("I threw your " + str(response1) + " at a spider! Sorry! New list: " + str(fruits) + "\n")
    response3 = input("Oh god, the spider's still alive! Pick a fruit from the list to throw at it! ")
    fruits.remove(str(response3))
    print("Yay, it's dead! and we have these fruits left: " + str(fruits) + "\n")
    print(border)

    print("--SERIES 3-- \n")
    for fruit in fruits[::]:
        response4 = input("Do you like " + fruit + "? (Y/N)")
        the_input = response4.lower()
        if the_input == 'n':
            fruits.remove(fruit)

    print("\nWe got rid of all the fruits you don't like, now we have: {}".format(fruits))
    print(border)

    print("--SERIES 4-- \n")
    fruits2 = fruits[::]
    [print(item) for item in fruits2]

    for x in fruits2[::]:
        word = list(x)
        print(word.reverse())


if __name__ == "__main__":
       main()