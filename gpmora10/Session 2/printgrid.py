def printgrid():
    for i in range (1,12):
        if i in (1 ,6, 11):
            print ("+ - - - - + - - - - +")
        else:
            print("|         |         |")

printgrid()