#exercise 11
#print "How old are you?",
#age = input()
#print "How tall are you?",
#height = input()
#print "How much do you weight?",
#weight = input()
#print "so, you are %r old, %r tall and %r heavy." %(age, height,weight)

#exercise 12
#age = input("How old are you? ")
#height = input("How tall are you? ")
#weight = input("How much do you weight? ")

#print ("so, you are %r old, %r tall and %r heavy." %(age, height,weight))

#exercise 13
#from sys import argv

#script,first,second,thrid = argv
#print("your script is ", script)
#print ("your first variable is ",first)
#print ("your second variable is ",second)
#print ("your third variable is ",third)

#exercise 14
#from sys import argv

#script,user_name = argv
#prompt = '> '

#print("Hi %s, I'm the %s script.") % (user_name,script)
#print("I's like to ask you a few questions.")
#print("Do you like me %s?")% user_name
#likes = raw_input("> ")

#print("Where do you live %s?") % user_name
#lives = raw_input("> ")

#print("What kind of computer do you have?")
#computer = raw_input("> ")

#print ("Alright, so you said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer. Nice.") %(likes, lives, computer)

# exercise 18
#def print_two(*args):
#    arg1,arg2,arg3= args
#    print ("arg1:%r, arg2:%r, arg3:%r") % (arg1,arg2,arg3)

#def print_two_again(arg1,arg2):
#    print ("arg1:%r, arg2:%r") %(arg1,arg2)

#def print_one(arg1):
#    print("arg1:%r") %arg1

#def print_none():
#    print("I got nothing.")

# print_two(1,"cc","ee")
# print_two_again("dd","cc")
# print_one("hello")
# print_none()

# exercise 19

# def cheese_and_cracker(a,b):
#     print("You have %d cheeses!") %a
#     print("You have %d boxes of crackers!") %b
#
# print("We cna just give the function numbers directly:")
# cheese_and_cracker(2,3)
#
# print("or, we can use variables from our script:")
# a=2
# b=3
#
#
# print ("We can even do math inside too:")
# cheese_and_cracker(10 + 20, 5 + 6)
#
#
# print ("And we can combine the two, variables and math:")
# cheese_and_cracker(a + 100, b + 1000)
# import sys
#
# def add(a,b):
#     print ("adding %d + %d") %(a,b)
#     c=int(int(a)+int(b))
#     return c
# print(add(5.7,6.4))
#
# def subtract(a, b):
#     print ("SUBTRACTING %d - %d" )% (a, b)
#     return a - b
#
# def multiply(a, b):
#     print ("MULTIPLYING %d * %d" )% (a, b)
#     return a * b
#
# def divide(a, b):
#     if b==0:
#        return sys.maxsize
#     else:
#         print ("DIVIDING %d / %d") % (a, b)
#         c=float(a)/float(b)
#         return c
#
# print ("Let's do some math with just functions!")
#
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 0)
#
# print ("Age: %d, Height: %d, Weight: %d, IQ: %f" )% (age, height, weight, iq)
#
#
# # A puzzle for the extra credit, type it in anyway.
# print  ("Here is a puzzle.")
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print ("That becomes: ", what, "Can you do it by hand?")


# exercise 29

# people = 20
# cats = 30
# dogs = 15
#
#
# if people < cats:
#     print ("Too many cats! The world is doomed!")
#
# if people > cats:
#     print ("Not many cats! The world is saved!")
#
# if people < dogs:
#     print ("The world is drooled on!")
#
# if people > dogs:
#     print ("The world is dry!")
#
#
# dogs += 5
#
# if people >= dogs:
#     print ("People are greater than or equal to dogs.")
#
# if people <= dogs:
#     print ("People are less than or equal to dogs.")
#
#
# if people == dogs:
#     print ("People are dogs.")

# exercise 30


# people = 30
# cars = 40
# trucks =15
#
# if cars>people:
#     print("use cars.")
# elif cars<people:
#     print("not use cars")
# else:
#     print("cannot decide")
#
# people+=20
#
# if cars>people:
#     print("use cars.")
# elif cars<people:
#     print("not use cars")
# else:
#     print("cannot decide")
#
#


# exercise 31

# print ("You enter a dark room with two doors.  Do you go through door #1 or door #2?")
#
# door = raw_input("> ")
# doorint = int(door)
# if doorint == 1:
#     print ("There's a giant bear here eating a cheese cake.  What do you do?")
#     print ("1. Take the cake.")
#     print "2. Scream at the bear."
#
#     bear = raw_input("> ")
#
#     if bear == "1":
#         print "The bear eats your face off.  Good job!"
#     elif bear == "2":
#         print "The bear eats your legs off.  Good job!"
#     else:
#         print "Well, doing %s is probably better.  Bear runs away." % bear
#
# elif door == "2":
#     print "You stare into the endless abyss at Cthulhu's retina."
#     print "1. Blueberries."
#     print "2. Yellow jacket clothespins."
#     print "3. Understanding revolvers yelling melodies."
#
#     insanity = raw_input("> ")
#
#     if insanity == "1" or insanity == "2":
#         print "Your body survives powered by a mind of jello.  Good job!"
#     else:
#         print "The insanity rots your eyes into a pool of muck.  Good job!"
#
# else:
#     print "You stumble around and fall on a knife and die.  Good job!"


#exercise 32
# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#
# # this first kind of for-loop goes through a list
# for number in the_count:
#     print "This is count %d" % number
#
# # same as above
# for fruit in fruits:
#     print "A fruit of type: %s" % fruit
#
# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print "I got %r" % i
#
# # we can also build lists, first start with an empty one
# elements = []
#
# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)
#
# # now we can print them out too
# for i in elements:
#     print "Element was: %d" % i

# exercise 33

i = 0
numbers = []

while i<6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    #if i==6:
        #break


print "The numbers: "

for num in numbers:
    print num
