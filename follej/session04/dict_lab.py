#!/usr/bin/env python3

d = dict(name='Chris', city='Seattle', cake='Chocolate')


def display_dictionary():
    for k, v in d.items():
        print("%s: %s" % (k, v))


if __name__ == '__main__':
    display_dictionary()
