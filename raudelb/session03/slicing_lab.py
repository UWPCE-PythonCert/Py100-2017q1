__author__ = 'raudel'


def last_first_exchange():
    seq = list(range(10))
    temp = seq[0]
    seq[0] = seq[len(seq)-1]
    seq[len(seq)-1] = temp
    return seq


def every_other_removed():
    seq = list(range(10))
    return seq[::2]


def first_last_four_removed():
    seq = list(range(10))
    return seq[1:-4:2]


def seq_reversed():
    seq = list(range(10))
    return seq[::-1]


def seq_middle_last_first():
    seq = list(range(12))
    q = len(seq)//3
    return seq[q:q+q], seq[q+q:], seq[:q]


def main():
    print(last_first_exchange())
    print(every_other_removed())
    print(first_last_four_removed())
    print(seq_reversed())
    print(seq_middle_last_first())


if __name__ == '__main__':
    main()