#!/usr/bin/env python3
#Write a function that prints the numbers from 1 to 100 inclusive but
#  for multiples of three print "Fizz" instead of the number
#  for multiples of five print "Buzz"
#  for multiples of both three and five print "FizzBuzz"
#http://uwpce-pythoncert.github.io/IntroToPython/exercises/fizz_buzz.html#exercise-fizz-buzz


input = [x for x in range(1,101)]
for i in input:
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
        continue
    if (i % 3 == 0):
        print("Fizz", end='')
    if (i % 5 == 0):
        print("Buzz", end='')
    print()

