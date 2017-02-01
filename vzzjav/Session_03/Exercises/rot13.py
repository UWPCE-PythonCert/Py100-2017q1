# Javier Vazquez
# ROT13
# Jan 31, 2017
# Description: hhttp://uwpce-pythoncert.github.io/IntroPython2016a/exercises/rot13.html

import os

def rot13(sentence):
    '''Encrypt and decrypt a text sentence'''
    decrypt = ""
    for letter in sentence:
        if letter.isupper():
            if ord(letter) >= 78:
                decrypt += chr(ord(letter)-13)
            else:
                decrypt += chr(ord(letter)+13)
        elif letter.islower():
            if ord(letter) >= 110:
                decrypt += chr(ord(letter)-13)
            else:
                decrypt += chr(ord(letter)+13)
        else:
            decrypt += letter
    return decrypt

def main():
    '''Only works with a text sentente'''
    sentence = "Zntargvp sebz bhgfvqr arne pbeare"
    print(rot13.__name__)
    print(rot13.__doc__)
    print(sentence + "\n" +  rot13(sentence))

    sentence = input("\nText to encrypt: ")
    print(sentence)
    print(rot13(sentence))

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()