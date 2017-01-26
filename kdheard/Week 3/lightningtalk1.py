#This is a UNIX Password Cracker from Chapter 1 of "Violent Python"
#There are minor variations in code and variable & function names compared to the book, these are noted in comments below

import crypt

def test_pass(crypt_pass):
    salt = crypt_pass[0:2]
    #This stores the encrypted password in a variable and strips away the first two characters, which is the salt
    dict_file = open('dictionary.txt', 'r')
    #Dictionary file which contains 479k known words, which will be hashed and compared with the encrypted password
    #source: https://github.com/dwyl/english-words
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word,salt)
        if (crypt_word==crypt_pass):
            print("[+] Found Password:"+ word)
        #else:
            #print"[-] Password Not Found. \n"
        #This is part of the book's code, but with such a large dictionary, the output becomes counterproductive printing this for each line

def main():
    passfile = open('passwords.txt')
    for line in passfile.readlines():
        if "user" in line:
            user = line.split(':')[1]
            print("[*] Cracking password for: " + user)
        if "password" in line:
            password = line.split(':')[1].strip('')
            print("[*] Encrypted password: " + password + "\n")
            test_pass(password)

if __name__ == "__main__":
    main()
