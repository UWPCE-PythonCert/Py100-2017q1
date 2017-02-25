#!/usr/bin/env python3

def main():
    sequence = ['Alice', 'Bob', 'Carl', 'Denny']
    sequence[0], sequence[-1] = sequence [-1], sequence[0]
    print(sequence)

    for list, item in sequence:
        if item.index() %2 == 0 :
            sequence.remove(item)
            print(sequence)


if __name__ == "__main__":
   main()
