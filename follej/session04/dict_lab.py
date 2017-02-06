#!/usr/bin/env python3

d = dict(name='Chris', city='Seattle', cake='Chocolate')


def display_dictionary():
    for k, v in d.items():
        print("%s: %s" % (k, v))
    print("")


def delete_item(param):
    d.pop(param)


def add_a_dict_entry(param):
    d.update(param)


def is_in_dictionary(param):
    print("%s is %sin dictionary" % (param, ("" if param in d else "not ")))


if __name__ == '__main__':
    display_dictionary()
    delete_item('cake')
    display_dictionary()
    add_a_dict_entry({'fruit': 'Mango'})
    display_dictionary()
    is_in_dictionary('cake')
    is_in_dictionary('fruit')
