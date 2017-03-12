__author__ = 'raudel'

# The input() function can generate two exceptions:
# EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.


def safe_input():
    try:

        test = int(input(' Please, enter a Real Value to generate EOFError exception or Ctrl+D (EOFError: '))

    except (EOFError, ValueError) as error_msg:

        print('Sorry, you entered a wrong type that produced an ', error_msg )


def main():
    safe_input()


if __name__ == '__main__':
    main()