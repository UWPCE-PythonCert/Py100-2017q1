#Lawrence Woods
# coding=utf-8
# This program pints the numbers between 1 to 100 inclusive.
# But for multiples of three the program prints “Fizz”
# instead of the number. For the multiples of five  the program
# prints “Buzz”. For numbers which are multiples of both three and
# five the program prints print “FizzBuzz” instead.


fizzbuzz = []

start = int(input("Enter Start Value"))
end = int(input("Enter End Value"))

for i in range(start, end + 1):
    entry = ''
    if i % 3 == 0:
        entry += "fizz"
    if i % 5 == 0:
        entry += "buzz"
    if i % 3 != 0 and i % 5 != 0:
        entry = i

    fizzbuzz.append(entry)

for i in fizzbuzz:
    print(i)