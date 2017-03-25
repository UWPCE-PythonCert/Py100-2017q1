#Kata Fourteen


students.txt

name: languages
Acharya, Madhumita: SQL, shell
Anderson, Paul G: basic, python, C++
Baumel, Bradley I: java, sql, python, html
Bearer, Jerry: bash, sql, asp, html
Briant, Paul S: python, html, php, sql, java
Casey, Paul A: C++, python,
Change, Simbarashe P: SQL
Chavis, Brandon: ruby, python, bash
Cowhey, Isaac: python, javascript, ruby, scala
Galande, Nachiket: R, java, php
He, Beatrice: SQL, R, SaS, C, shell
Hefner, Jack M: python, perl, C++
Hicks, Josh: C#, bash , perl
Hollis, Adam: python, basic, html, actionscript, php
Latif, Shu A: python, bash, html
Mandava, Sasi: C, C++
McGhin, Spencer G: python, sql, R, html
Muralidharan, Sharmila: cobol, sql,
Naik, Ninad: C++, python
Pena, Sheree: swift
Raina, Jay N: SQL, R, python
Robison, Charles E: SQL, python,
Silva, Enrique R: python, sql
Tobey, David E: bash, qbasic, sql
Truong, Alexander C: pyton , htl, xml
Vosper, Paul: C#, macscript, python
Weidner, Matthew T: German, python, html
Williams, Marcus D: python
Wong, Darryl: perl, php
Yang, Minghao: None
Hagi, Abdishu: python, bash


schedule.py

"""
Schedule students for lightning talks, fall 2015
"""
import random

students = open('students.txt').readlines()

# remove the header line
del students[0]

# strip the whitespace
students = [line.strip() for line in students]

# remove the languages, colon, etc.
students = [line.split(":")[0] for line in students]

# reverse the first, last names
# separate them:
students = [line.split(",") for line in students]
# put them back together
students = ["{} {}".format(first.strip(), last) for last, first in students]

# put them in random order
random.shuffle(students)

# make a list from 1 to 10
weeks = list(range(2, 11))

# make three of them...
weeks = weeks * 4

# put the students together with the weeks
schedule = zip(weeks, students)

# sort it for output
schedule = sorted(schedule)

# write it to a file (and print to screen)
with open('schedule.txt', 'w') as outfile:
    for week, student in schedule:
        line = 'week {}: {}\n'.format(week, student)
        print(line)
        outfile.write(line)