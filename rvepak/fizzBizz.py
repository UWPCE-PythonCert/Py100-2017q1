import argparse

parser = argparse.ArgumentParser(
    description='This is a script to generate FizzBuzz')
parser.add_argument('-m', help='maxNumber', required=True)
args = parser.parse_args()

maxNumber = args.m


def printNumbers(maxNumber):
    '''
    this method prints the numbers upto MaxNumber (inclusive)
    for multiples of three print “Fizz” instead of the number
    For the multiples of five print “Buzz”.
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
    '''
    for i in range(1, maxNumber + 1):
        if i % 5 == 0 and i % 3 == 0:
            i = 'FizzBuzz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 3 == 0:
            i = 'Fizz'
        print(i)


printNumbers(int(maxNumber))
