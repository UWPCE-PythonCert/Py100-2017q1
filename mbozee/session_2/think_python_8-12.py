
# Think Python
# http://greenteapress.com/thinkpython/html/


####################
# Chapter 8: Strings
####################

# Exercise 10

def is_palindrome(word):
    """Return True of word is a palindrome."""
    return word == word[::-1]

print(is_palindrome('tacocat')) # tacocat is a palindrome
print(is_palindrome('banana')) # banana is not a palindrome


# Exercise 11

# Function 1 is correct. It loops through each letter
# and returns True there is a lowercase letter.

# Function 2 is incorrect. It loops through each letter,
# but returns the string 'True' if the string 'c' is lowercase
# and returns the string 'False' if the string 'c' is not lowercase.

# Function 3 is correct. It returns the variable flag,
# which is set to True if a letter is lowercase and False
# if a letter is not lowercase.

# Function 4 is correct. If a letter is lowercase, the flag
# variable with be set to True. Otherwise, it will default
# to its original value of False. Since True takes precedence
# over False, this performs correctly.

# Function 5 is incorrect. It returns False all letters are
# lowercase, and returns True if there is an uppercase letter.


# Exercise 12

# To be completed at a later time.
