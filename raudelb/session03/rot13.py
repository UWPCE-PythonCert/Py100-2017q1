__author__ = 'raudel'


def decode(my_text, alph):

    decoded_text = ''

    for i in my_text:
        if i in alph:
            value_index = alph.index(i)
            value_shifted = value_index - 13
            temp = alph.__len__()
            if value_shifted > 0:
                decoded_text += alph[value_shifted]
            else:
                #value_dif = value_shifted - character_list.__len__()
                decoded_text += alph[value_shifted]
        else:
            decoded_text += i

    return decoded_text


def rot13(my_text, alph):

    cipher = ''

    for i in my_text:
        if i in alph:
            value_index = alph.index(i)
            value_shifted = value_index + 13
            temp = alph.__len__()
            if value_shifted < alph.__len__():
                cipher += alph[value_shifted]
            else:
                value_dif = value_shifted - alph.__len__()
                cipher += alph[value_dif]
        else:
            cipher += i

    return cipher


def main():
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))
    for i in range(65, 91):
        alphabet.append(chr(i))


    plain_text = "Be careful with the cat of your neighbour his name is  Rainbow and he is pupping a lot"
    cipher_text = rot13(plain_text, alphabet)
    print(cipher_text)

    test_text = 'Zntargvp sebz bhgfvqr arne pbeare'

    my_decoded_text = decode(cipher_text, alphabet)
    print('The text decoded is:', my_decoded_text)

    print('And your secret text is:', decode(test_text, alphabet))

if __name__ == '__main__':
    main()