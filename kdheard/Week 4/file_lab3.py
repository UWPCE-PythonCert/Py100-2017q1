from os import chdir

def main():

    chdir('/home/vagrant/Documents/Py100/Py100-2017q1/kdheard/Week 4')
    students = open('students.txt', 'r')

    ''' The assignment says to generate a list of languages that have been used.
    The existing students.txt file does not, so I made up languages for everyone.
    '''
    list_of_languages = ['Python']
    for line in students.readlines():
        line = line.strip('\n')
        new_line = line.split (' - ')[1]
        print(new_line)

if __name__ == "__main__":
    main()
