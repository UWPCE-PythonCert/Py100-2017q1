import argparse

parser = argparse.ArgumentParser(
    description='This is a script to generate nth value of fibonacci series')
parser.add_argument('-n', help='position(starting from 0)', required=True)
args = parser.parse_args()

position = args.n

print('Returning position - {}  value of fibonacci series (starting from 0)'.
      format(position))


def fib(position):
    '''
    this function returns the nth value in fibonacci series starting from 0
    '''
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fib(position - 1) + fib(position - 2)


def main():
    print(fib(int(position)))


if __name__ == '__main__':
    main()
