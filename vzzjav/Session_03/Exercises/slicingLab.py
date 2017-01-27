# Javier Vazquez
# Grid Printer
# Jan 26, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/slicing.html

import string, math

def exchangeFL(sequence):
    if isinstance(sequence, str):
        return sequence[-1] + sequence[1:len(sequence)-1] + sequence[0]

def removedItem(sequence):
    if isinstance(sequence, str):
        return sequence[0:len(sequence):2]


def remover4fl_n(sequence, n):
    if isinstance(sequence, str):
        return sequence[4:-4:1]

def reverse(sequence):
    if isinstance(sequence, str):
        return sequence[::-1]

def thirds(sequence):
    if isinstance(sequence, str):
        if len(sequence) % 3 == 0:
            return sequence[len(sequence)/3:(len(sequence)/3)*2]
        else:
            return sequence[math.ceil(len(sequence) / 3):math.ceil((len(sequence) / 3) * 2)] + \
                   sequence[math.ceil((len(sequence) / 3) * 2):] + \
                   sequence[0:math.ceil(len(sequence) / 3)]





def main():
    print(exchangeFL(string.ascii_lowercase))
    print(removedItem(string.ascii_lowercase))
    print(remover4fl_n(string.ascii_lowercase, 10))
    print(reverse(string.ascii_lowercase))
    print(thirds(string.ascii_lowercase))

if __name__ == '__main__':
    main()
