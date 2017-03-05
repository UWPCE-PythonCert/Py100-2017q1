__author__ = 'raudel'


# Write a little script that reads that file,
# and generates a list of all the languages that have been used.

def main():

    f = open('students.txt')
    lines = f.readlines()
    l = lines.__len__()
    my_set = set()
    total_languages = []
    for i in range(l-1):
        i += 1
        index = lines[i].index(':') + 2
        length = lines[i].__len__()
        line = lines[i]

        sub_str = line[index:length]

        sub_str = sub_str.strip('\n')
        sub_str = sub_str.replace(' ', '') # for one reason: sub_str.trip() does not work, I used replace method

        languages_l = sub_str.split(',')
        total_languages += languages_l
        temp_set = set(languages_l)
        my_set = my_set.union(temp_set)
        my_set = my_set.difference({''})

        list_languages = list(my_set)


    print('The list of all languages are:', list_languages)

    for item in total_languages:
        if item == '':
            total_languages.remove(item)

    # Extra credit: keep track of how many students specified each language.

    for l in list_languages:
        print('\n %s student(s) specified %s language.' % (total_languages.count(l), l))


if __name__ == '__main__':
    main()

