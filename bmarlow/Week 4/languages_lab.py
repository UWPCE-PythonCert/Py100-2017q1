#!/usr/bin/env python

def main():
    """main function"""
    student_dict = {}
    file = open('students.txt', 'r')

    while True:
        # read the line
        line = file.readline()

        # if there is nothing to read, break
        if not line:
            break

        # get rid of the newlines
        line = line.strip('\n')

        # break the students from the languages
        stu_lang_list = line.split(':')

        # create a temp dict to store the values
        tempdict = {stu_lang_list[0]: stu_lang_list[1]}

        # update our main dictionary
        student_dict.update(tempdict)

    # extract all of the languages from our dict
    languages = student_dict.values()

    # create an empty set for making unique languages, we'll let python do the unique work :-)
    unique_languages = set()
    counted_languages = {}

    # technically the 'language' could be plural, but this sounded better than:
    # for languages in languagess
    for language in languages:

        # split out the students langauges into a list
        list = language.split(',')

        # for each language the student knows
        for item in list:

            # get rid of the leading whitespace
            item = item.lstrip()

            # shove that particular language into the set (and let the set do the unique clean up
            unique_languages.update([item])

            # if the langauge isn't in the dictionary add it with a qty of 1
            if not item in counted_languages:
                tempdict = {item : 1}

            # if the langauge is in the diction update its value to + 1
            elif item in counted_languages:
                qty = counted_languages[item] + 1
                tempdict = {item: qty}
            counted_languages.update(tempdict)

    # technically 'langauges' isn't a language
    # yes I could've avoided this by starting to read the file at a certain line
    # however I'd already committed to this while loop :-)
    counted_languages.pop('languages', None)

    #for each of the counted languages, print the name and the value
    for key in counted_languages:
        value = str(counted_languages[key])
        print(str(key) + ' ' + value)

if __name__ == '__main__':
    main()

