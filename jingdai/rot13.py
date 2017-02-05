#rot13
import string
if __name__ == '__main__':


    def rot13(string):
        encoding = string.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


        return print(string.translate(encoding))


rot13('Zntargvp sebz bhgfvqr arne pbeare')

