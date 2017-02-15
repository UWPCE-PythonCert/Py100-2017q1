#!/usr/bin/env python3

s2 = set()
s3 = set()
s4 = set()


def create_sets():
    global s2, s3, s4
    for i in range(0, 21):
        if i % 2 == 0:
            s2.update([i])
        if i % 3 == 0:
            s3.update([i])
        if i % 4 == 0:
            s4.update([i])


def display_sets():
    print(s2)
    print(s3)
    print(s4)


def is_subset(set1, set2):
    print(set1.issubset(set2))


if __name__ == '__main__':
    create_sets()
    display_sets()
    is_subset(s3, s2)
    is_subset(s4, s2)
    s5 = set(list('Python'))
    print(s5)
    f1 = frozenset(list('marathon'))
    print(f1)
    print(s5.union(f1))
    print(s5.intersection(f1))
