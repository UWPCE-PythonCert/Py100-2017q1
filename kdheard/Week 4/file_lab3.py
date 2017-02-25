from os import chdir

def main():

    chdir('/home/vagrant/Documents/Py100/Py100-2017q1/kdheard/Week 4')
    students = open('students.txt', 'r')
    known_languages = set()

    ''' The assignment says to generate a list of languages that have been used.
    However, the existing students.txt file does not include languages yet, so I made up languages for everyone.
    '''
    for line in students.readlines():
        line = line.strip('\n')
        new_line = line.split(' - ')[-1]
        known_languages.add(str(new_line))
    print(known_languages)

if __name__ == "__main__":
    main()