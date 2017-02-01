
# def rot13():
#     """Return string with each letter replaced by the letter 13 away it."""
#     string = "Zntargvp sebz bhgfvqr arne pbeare"
#     string_rot13 = string.maketrans(string, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
#     print(string_rot13)

import codecs


def rot13():
    """Return string with each letter replaced by the letter 13 away it."""
    print(codecs.encode('Zntargvp sebz bhgfvqr arne pbeare', 'rot_13'))


if __name__ == '__main__':
    rot13()