__author__ = 'raudel'

import pathlib


def main():

    # write a program which prints the full path to all files in the current directory, one per line

    print('This is the full path to all files in the current directory...')

    path = pathlib.Path.cwd()

    print(path)

    for f in path.iterdir():
        print(f)

    # write a program which copies a file from a source, to a destination
    # (without using shutil, or the OS copy command)

    # This should work for any kind of file,
    # so you need to open the files in binary mode:
    # open(filename, 'rb') (or 'wb' for writing).

    # Test it with both text and binary files (maybe jpeg or??)

    print('You are coping a file from source to destination...')

    file_name_list = ['file_to_copy.html', 'picture.jpg']

    for file_name in file_name_list:

        source = pathlib.Path(str(file_name)).resolve()

        destination = 'coping_files_test/' + str(file_name)

        with open(str(destination), 'wb') as d:
            with open(str(source), 'rb') as s:
                byte = s.read(1)
                while byte:
                    d.write(byte)
                    byte = s.read(1)


if __name__ == '__main__':
    main()