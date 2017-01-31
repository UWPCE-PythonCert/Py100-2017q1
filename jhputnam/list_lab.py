#!/usr/bin/env python3


"""Module for list lab"""


def main():
    """
    Main function for list lab. Nothing fancy this time.
    Just serially shoving each task into main one piece at a time.
    Saving fancy for the soul-destroying Mailroom.
    Reading this top to bottom should match each task on the list
    lab in order.
    """

    # Make the list.
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    print(fruits, "\n")

    # Add a new fruit to the end.
    fruits.append(input("Enter a new fruit, you fruit!:\n"))

    print(fruits, "\n")

    # Grab a number from the user, and enforce some sanity.
    while True:
        try:
            number = int((input("Give me a number!!!\n")))
            if number <= 0:
                print("Numbers greater than zero please. Thx.")
                continue
            break
        except ValueError:
            print("My GOD. That's not a number at all. What are you doing?!")

    # Match the number with the corresponding fruit in the list.
    try:
        print("The number {} corresponds to {} in the list.\n".format(number,
              fruits[number - 1]))
    except IndexError:
        print("There's no fruit with that number.\n")

    # Arbitarily add another fruit to the beginning of the list.
    print("Marvel in awe as I insert Tomatoes into the list!\n")
    fruits = ["Tomatoes"] + fruits
    print(fruits, "\n")

    # Do it again because reasons.
    print("Be amazed as I again insert Watermelons into the list. "
          "Mind == blown.\n")
    fruits.insert(0, "Watermelons")
    print(fruits, "\n")

    # Print all the fruits that start with the letter P.
    for fruit in fruits:
        if fruit[0] == "P":
            print(fruit)
    print("\n")

    # Display the list again.
    print(fruits, "\n")

    # Pop that fool.
    fruits.pop()
    print(fruits, "\n")

    # Delete a fruit.
    while True:
        fruit = input("Enter a fruit to remove from the list:\n")
        try:
            match = next(x for x in fruits if x == fruit)
            fruits.remove(match)
            break
        except StopIteration:
            print("No fruit with that name in the list\n")
            continue
    print(fruits)

    # Double the list and remove all matches.
    doubled = []
    for fruit in fruits:
        doubled.extend([fruit, fruit])
    print(doubled, "\n")

    while True:
        fruit = input("Enter a fruit to remove again:\n")
        if fruit in doubled:
            newlist = [x for x in doubled if x != fruit]
            break
        else:
            print("No fruit with that name in the list\n")
            continue
    print(newlist, "\n")

    # Re-make the original list list.
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    # Copy the list, because removing items from the list you're iterating
    # over is bad news bears.
    fruits_copy = list(fruits)

    for fruit in fruits_copy:
        while True:
            answer = input("Do you like {}, y/n? "
                           .format(fruit).lower()).lower()
            if answer == "yes" or answer == "y":
                break
            elif answer == "no" or answer == "n":
                fruits.remove(fruit)
                break
            else:
                print("Please answer yes or no (y or n also acceptable).\n")
                continue

    print(fruits, "\n")

    # Copy the list, overwriting the one from earlier.
    # Build the new list from the old, reversing the letters as we go.
    fruits_copy = []

    # Remake the original list again.
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    for fruit in fruits:
        fruits_copy.append(fruit[::-1])

    # For some reason, the lab asks to delete the last item of the original
    # list again, even though we did it earlier.
    fruits.pop()

    print("Original list minus the last item:")
    print(fruits)
    print("Copy of the list:")
    print(fruits_copy)


if __name__ == "__main__":
    main()
