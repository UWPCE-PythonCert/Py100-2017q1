#!/usr/bin/env python

import os

def listfiles():
    """function to list absolute path of all files in current directory"""
    cwd = os.getcwd()
    files = os.listdir(cwd)
    for file in files:
        print(os.path.abspath(file))


def filecopy():
    """function for doing a streaming binary file copy"""
    source = input('Please enter the name of the file to be copied:\n')
    if not os.path.isfile(source):
        print('Sorry, source file does not exist.\n')
        filecopy()
        return
    destfile = input('Please enter the name that you would like for the destination file:\n')

    dest = open(destfile, 'bw+')
    with open(source, 'rb') as file:
        print('Copying file...', end='', flush=True)
        while True:
            buffer = file.read(64)
            print('.', end='', flush=True)
            if not buffer:
               print('')
               print('File finished copying!')
               break
            print('.', end='', flush=True)
            dest.write(buffer)


def main():
    """main function for this lab"""
    print('Please make a selection:')
    print('1.  List the files in the current directory')
    print('2.  Use Brandon\'s patent pending (just kidding) streaming file copy')
    choice = input('')
    if choice == '1':
        listfiles()
    elif choice == '2':
        filecopy()
    else:
        print('Sorry, ' + choice + ' is not a valid selection, please choose 1 or 2')
        main()
        return

if __name__ == '__main__':
    main()