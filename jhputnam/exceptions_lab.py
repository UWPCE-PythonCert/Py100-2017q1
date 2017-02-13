#!/usr/bin/env python3

"""Exceptions Lab"""


def safe_input(label):
    """
    Wrapper for input.
    Arguments:
    label: Prompt text for data input.
    Returns input data.
    """

    while True:

        try:
            datas = input(label)

        except EOFError:
            print()
            continue
        except KeyboardInterrupt:
            print()
            continue
        break

    return datas


def main():
    """Main function for the program"""

    datas = safe_input("input some stuff: ")

    print(datas)


if __name__ == '__main__':
    main()
