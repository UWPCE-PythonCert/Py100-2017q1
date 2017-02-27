'''
Create a dictionary containing “name”, “city”, and “cake” for “Matt” from “Seattle” who likes “Chocolate”.
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value. (upper and lower case?).
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets.
'''


def main():
    # Create a dictionary containing “name”, “city”, and “cake” for “Matt” from “Seattle” who likes “Chocolate”.
    our_dict = {"Name": "Matt", "City": "Seattle", "Cake": "Chocolate"}
    print("Dictionary Contents: {} ".format(our_dict))  # Display the dictionary.
    #  Delete the entry for “cake”.
    for key, item in our_dict.items():
        if key == "Cake":
            del our_dict["Cake"]
            break
    print("Deleting cake: {}".format(our_dict))  # Display the dictionary.
    #  Add an entry for “fruit” with “Mango” and display the dictionary.
    our_dict["Fruit"] = "Mango"
    print("Adding fruit: {}".format(our_dict))

    print("Keys: {}".format(our_dict.keys()))  # Display the dictionary keys.
    print("Values: {}".format(our_dict.values()))  # Display the dictionary values.

    for key, item in our_dict.items():
        if key == 'Cake':
            print("\nHave some cake")  # Suckers we already know there is no cake
        elif item == 'Mango':
            print("\nSorry, we have no cake. Would you like some mango?")



if __name__ == "__main__":
    main()
