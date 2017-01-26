#!/usr/bin/env python3

def main()
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("These are the current fruits we have: " + str(fruits))
    response1 = raw_input("What is your favorite fruit? ")
    fruits.append(response1)
    print("Thanks! We added it to our fruits: " + str(fruits))

    response2 = raw_input("Give me a number: ")
    print("This was your number: " + str(response2))
    print("This is the fruit in the list that it responds to: " + fruits[int(response2)])

    fruits = fruits + ["Watermelon"]
    print("I added a fruit too: " + str(fruits))


#if __name__ == "__main__":
 #   main()