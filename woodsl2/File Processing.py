'''
File Processing
'''



# here all three part in same example.

from os import listdir
from os.path import isfile, join, abspath


# part first list files in current dir
for f in listdir('.'):
    if isfile(f):
        print(abspath(f))

# part 2 copy program
file_name = input("Enter a file name to copy: ")
copy_name = input("Enter destination file name: ")

def copyfileobj(source, dest, buffer_size=1024*1024):
    """
    Copy a file from source to dest. source and dest
    must be file-like objects, i.e. any object with a read or
    write method, like for example StringIO.
    """
    while 1:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def copyfile(source, dest):
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        copyfileobj(src, dst)


copyfile(file_name, copy_name)

# part 3 list languages with count of students
lang_dict = {}
with open("students.txt", "r") as fp:
    for line in fp:
        line = line.rstrip()
        (student, languages) = line.split(":")
        l = languages.split(",")
        for language in l:
            language = language.strip()
            if language == "None":
                continue
            if language in lang_dict:
                lang_dict[language] = lang_dict[language] + 1
            else:
                lang_dict[language] = 1

for language in lang_dict:
    print(language + " is known to " + str(lang_dict[language]) + " students")

