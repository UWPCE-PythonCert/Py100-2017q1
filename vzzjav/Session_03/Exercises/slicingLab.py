# Javier Vazquez
# Grid Printer
# Jan 26, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/slicing.html

import string, math, os

def exchangeFL(sequence):
    '''Returns a sequence with the first and last items exchanged.'''
    if isinstance(sequence, str):
        return sequence[-1] + sequence[1:len(sequence)-1] + sequence[0]

def removedItem(sequence):
    '''Returns a sequence with every other item removed'''
    if isinstance(sequence, str):
        return sequence[0:len(sequence):2]

def remover4fl(sequence):
    '''Returns a sequence with the first and last 4 items removed, and every other item in between'''
    if isinstance(sequence, str):
        return sequence[4:-4:1]

def reverse(sequence):
    '''Returns a sequence reversed (just with slicing)'''
    if isinstance(sequence, str):
        return sequence[::-1]

def thirds(sequence):
    '''Returns a sequence with the middle third, then last third, then the first third in the new order'''
    if isinstance(sequence, str):
        if len(sequence) % 3 == 0:
            return sequence[int(len(sequence)/3):int((len(sequence)/3)*2)] + \
                    sequence[int((len(sequence) / 3) * 2):]  + \
                    sequence[0:int(len(sequence) / 3)]
        else:
            return sequence[math.ceil(len(sequence) / 3):math.ceil((len(sequence) / 3) * 2)] + \
                   sequence[math.ceil((len(sequence) / 3) * 2):] + \
                   sequence[0:math.ceil(len(sequence) / 3)]

def main():
    '''Only works with string type sequence'''
    print("Original sequence: "+ string.ascii_lowercase + "\n")
    print(exchangeFL.__name__)
    print(exchangeFL.__doc__)
    print(exchangeFL(string.ascii_lowercase),"\n")
    print(removedItem.__name__)
    print(removedItem.__doc__)
    print(removedItem(string.ascii_lowercase),"\n")
    print(remover4fl.__name__)
    print(remover4fl.__doc__)
    print(remover4fl(string.ascii_lowercase),"\n")
    print(reverse.__name__)
    print(reverse.__doc__)
    print(reverse(string.ascii_lowercase),"\n")
    print(thirds.__name__)
    print(thirds.__doc__)
    print(thirds(string.ascii_lowercase),"\n")

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    print(dir(sys.modules[__name__]))
    main()
