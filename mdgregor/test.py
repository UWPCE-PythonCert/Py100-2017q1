# First solution to FizzBuzz. This is based on the code I wrote for the Grid Printer lab
# The idea is that every nth number that is divisible by 3 and 5 is always divisible by 15 and no number divisible by 15 isn't also divisible by 3 and 5
# So I have a for loop that runs through a user-defined range and prints FizzBuzz, Fizz, Buzz or n depending on the result of the mod function.
# I've stored this in a function so I could write multiple solutions without printing 1-100 multiple times in the same Python file

list_one = []
list_two = []

def FizzBuzzOne(RangeFloor,RangeCeiling):
    for i in range(RangeFloor,RangeCeiling+1):
        if i%15 == 0:
            list_one.append("FizzBuzz")
        elif i%3 == 0:
            list_one.append("Fizz")
        elif i%5 == 0:
            list_one.append("Buzz")
        else:
            list_one.append(i)


# Second solution to FizzBuzz
# This creates a list of valid integers that should return Fizz and/or Buzz
# It then runs through a user-defined range and checks if each value in that range should return Fizz and/or Buzz, and prints accordingly

def FizzBuzzTwo(RangeFloor,RangeCeiling):
    # First, we'll define our variables.
    # f and b will be used to generate lists of valid integers to return Fizz and Buzz
    # Fizz and Buzz will be lists that hold those values
    f = 0
    b = 0
    Fizz = []
    Buzz = []

    # Next, we'll generate those lists of integers that should return Fizz and Buzz
    while f <= RangeCeiling:
        f += 3
        Fizz.append(f)
    while b <= RangeCeiling:
        b += 5
        Buzz.append(b)

    # Finally, we will iterate through the user-defined range and test which values match those in Fizz and/or Buzz and print accordingly
    for i in range(RangeFloor,RangeCeiling+1):
        if i in Fizz:
            if i in Buzz:
                list_two.append("FizzBuzz")
            else:
                list_two.append("Fizz")
        elif i in Buzz:
            list_two.append("Buzz")
        else:
            list_two.append(i)


FizzBuzzOne(1,100)
FizzBuzzTwo(1,100)
print(list_one)
print(list_two)

assert list_one == list_two
