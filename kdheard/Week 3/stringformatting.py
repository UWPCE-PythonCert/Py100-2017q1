#!/usr/bin/env python3
from decimal import Decimal
def main(fileno, dec, scientific_notation):
    second_item = ("{0:.2f}".format(dec))
    third_item = ("{0:.2e}".format(Decimal(scientific_notation)))
    print('file_00{}: {}, {}'.format(fileno,second_item,third_item))

if __name__ == "__main__":
    main(2, 123.4567, 10000)
