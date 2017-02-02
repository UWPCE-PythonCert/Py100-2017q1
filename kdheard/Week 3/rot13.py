#!/usr/bin/env python3
plaintext = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ"
ciphertext = "nopqrstuvwxyzabcdefghijlkmNOPQRSTUVWXYZABCDEFGHIJKLM"

def main():

    menu = input("Enter 1 to encrypt, 2 to decrypt, 3 to exit > ")
    if menu == "1":
        rot13()
    elif menu == "2":
        decrypt()
    elif menu == "3":
        quit()


def rot13():
    cipher = str.maketrans(plaintext,ciphertext)

    prompt = input("Enter the text to be encrypted: ")
    print(prompt.translate(cipher))
    main()

def decrypt():

    anti_cipher = str.maketrans(ciphertext,plaintext)

    prompt = input("Enter the text to be decrypted: ")
    print(prompt.translate(anti_cipher))
    main()


if __name__ == "__main__":
    main()