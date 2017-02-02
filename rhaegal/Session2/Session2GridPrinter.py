def gridprinter(size=5, squares=2):
    for line in range((size*squares)+1):
        if line%size==0:
            print (squares*("+"+"-"*size) + "+")
        else:
            print (squares*("|"+" "*size) + "|")

gridprinter()