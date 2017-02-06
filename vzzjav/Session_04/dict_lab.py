# Javier Vazquez
# Grid Printer
# Jan 29, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/dict_lab.html

import os

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


if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()