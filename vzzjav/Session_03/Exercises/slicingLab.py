# Javier Vazquez
# Grid Printer
# Jan 26, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/slicing.html

import string, math

def exchangeFL(sequence):
    '''Return a sequence with the first and last items exchanged.'''
    if isinstance(sequence, str):
        return sequence[-1] + sequence[1:len(sequence)-1] + sequence[0]

def removedItem(sequence):
    '''Return a sequence with every other item removed'''
    if isinstance(sequence, str):
        return sequence[0:len(sequence):2]


def remover4fl(sequence):
    '''Return a sequence with the first and last 4 items removed, and every other item in between'''
    if isinstance(sequence, str):
        return sequence[4:-4:1]

def reverse(sequence):
    '''Return a sequence reversed (just with slicing)'''
    if isinstance(sequence, str):
        return sequence[::-1]

def thirds(sequence):
    '''Return a sequence with the middle third, then last third, then the first third in the new order'''
    if isinstance(sequence, str):
        if len(sequence) % 3 == 0:
            return sequence[len(sequence)/3:(len(sequence)/3)*2] + \
                   sequence[math.ceil((len(sequence) / 3) * 2):] + \
                   sequence[0:math.ceil(len(sequence) / 3)]



        else:
            return sequence[math.ceil(len(sequence) / 3):math.ceil((len(sequence) / 3) * 2)] + \
                   sequence[math.ceil((len(sequence) / 3) * 2):] + \
                   sequence[0:math.ceil(len(sequence) / 3)]





def main():
    print(exchangeFL.__doc__)
    print(exchangeFL(string.ascii_lowercase),"\n")
    print(removedItem.__doc__)
    print(removedItem(string.ascii_lowercase),"\n")
    print(remover4fl.__doc__)
    print(remover4fl(string.ascii_lowercase),"\n")
    print(reverse.__doc__)
    print(reverse(string.ascii_lowercase),"\n")
    print(thirds.__doc__)
    print(thirds(string.ascii_lowercase),"\n")

if __name__ == '__main__':
    main()
