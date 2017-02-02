
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz" instead.


def fizzBuzz(ostream):

    for ii in range(1, 101):

        if ii % 3 == 0 and ii % 5 == 0:
            ostream.write("FizzBuzz\n")
            continue

        if ii % 3 == 0:
            ostream.write("Fizz\n")
            continue

        if ii % 5 == 0:
            ostream.write("Buzz\n")
            continue

        ostream.write(str(ii)+"\n")