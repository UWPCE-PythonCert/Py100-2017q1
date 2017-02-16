#!/usr/bin/env python3
d = {}


def create_initial_dictionary():
    global d
    d = dict(name='Chris', city='Seattle', cake='Chocolate')


def display_dictionary(param):
    for k, v in param.items():
        print("%s: %s" % (k, v))
    print("")


def delete_item(param):
    d.pop(param)


def add_a_dict_entry(param):
    d.update(param)


def is_in_dictionary(param):
    print("%s is %sin dictionary" % (param, ("" if param in d else "not ")))
    print("")


def make_letter_count_dictionary(param):
    d2 = {}.fromkeys(d)
    for key in d2:
        d2[key] = d[key].count(param)
    return d2


if __name__ == '__main__':
    create_initial_dictionary()
    display_dictionary(d)
    delete_item('cake')
    display_dictionary(d)
    add_a_dict_entry({'fruit': 'Mango'})
    display_dictionary(d)
    is_in_dictionary('cake')
    is_in_dictionary('fruit')
    create_initial_dictionary()
    display_dictionary(d)
    d2 = make_letter_count_dictionary('t')
    display_dictionary(d2)
