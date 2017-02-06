# Javier Vazquez
# Grid Printer
# Jan 29, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/dict_lab.html

import os, string

def main():
    cakeDict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(cakeDict)
    del cakeDict["cake"]
    print(cakeDict)
    cakeDict["fruit"] = "Mango"
    print(cakeDict)
    print(cakeDict.keys())
    print(cakeDict.values())
    print("cake" in cakeDict.keys())
    print("Mango" in cakeDict.values())
    cakeDict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    i = 0
    for key in cakeDict.keys():
        cakeDict[key] = i
        i += 1
    print(cakeDict)

    s2 = set(range(0,21,2))
    s3 = set(range(0,21,3))
    s4 = set(range(0,21,4))
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

    s= set()
    print(s)
    for letter in string.ascii_lowercase:
        s.update(letter)
    print(s)

    fs = frozenset("marathon")

    print(fs.union(s))
    print(fs.intersection(s))


if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()