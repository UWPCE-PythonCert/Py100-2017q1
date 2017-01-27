# Javier Vazquez
# Grid Printer
# Jan 26, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/slicing.html

import string

def exchangeFL(sequence):
    if isinstance(sequence, str):
        outputSeq = ""
        for i in range(len(sequence)):
            if i == 0:
                outputSeq += sequence[len(sequence)-1]
            elif i == len(sequence) - 1:
                outputSeq += sequence[0]
            else:
                outputSeq += sequence[i]
        return outputSeq

def removedItem(sequence, n):
    if isinstance(sequence, str):
        outputSeq = ""
        for i in range(len(sequence)):
            if i < n-1:
                outputSeq += sequence[i]
            elif i == n-1:
                outputSeq += ""
            elif i > n-1:
                outputSeq += sequence[i]
        return outputSeq

def remover4fl_n(sequence, n):
    if isinstance(sequence, str):
        outputSeq = ""
        for i in range(4, len(sequence)-4):
            if i == n-1:
                outputSeq += ""
            else:
                outputSeq += sequence[i]
        return outputSeq

def reverse(sequence):
    if isinstance(sequence, str):
        outputSeq = ""
        for i in range(len(sequence), -1, -1):
            outputSeq += str(i)
        return outputSeq



def main():
    print(exchangeFL(string.ascii_lowercase))
    print(removedItem(string.ascii_lowercase, 10))
    print(remover4fl_n(string.ascii_lowercase, 10))
    print(reverse(string.ascii_lowercase))

if __name__ == '__main__':
    main()
