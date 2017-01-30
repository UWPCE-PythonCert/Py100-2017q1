#!/usr/bin/env python3

import string
import copy
s = string

def main():
    print("--SERIES 1--")
    border = "- - - - - - - - - - - - - - - - - - - - - - - - - - - "
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("These are the current fruits we have: " + str(fruits) + "\n")
    response1 = input("What is your favorite fruit? ")
    fruits.append(response1)
    print("Thanks! We added it to our fruits: " + str(fruits) + "\n")

    response2 = input("Give me a number from 0 - 4: ")
    print("This was your number: " + str(response2))
    print("This is the fruit in the list that it responds to: " + fruits[int(response2)] + "\n")
    fruits = ["Watermelon"] + fruits
    print("I added Watermelon: " + str(fruits) + "\n")
    fruits.insert(0,"Persimmons")
    print("I added Persimmons too: " + str(fruits) + "\n")
    print("Here are all our fruits that start with 'P': " + str(filter(lambda x: 'P' in x,fruits)) + "\n")
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
    for x in range(len(fruits)):
        prompt = str(fruits[x])
        response4 = input("Do you like " + prompt + "? (Y/N)")
        if (s.lower(str(response4))) == "n":
            try:
                fruits.remove(str(prompt))
            except:
                pass
        elif (s.lower(str(response4))) == "y":
            try:
                prompt = str(fruits[x + 1])
            except:
                pass
    print("\nWe got rid of all the fruits you don't like, now we have: " + str(fruits))
    print(border)

    print("--SERIES 4-- \n")
    fruits2 = copy.copy(fruits)
    print(fruits2)
    for x in range(len(fruits2)):
        word = list(str(fruits[x]))
        print(word.reverse())





if __name__ == "__main__":
   main()