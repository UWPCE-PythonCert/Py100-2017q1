size=5
for line in range(11):
    if line%size==0:
        print "+"+"-"*size+"+"+"-"*size+"+"
    else:
        print "|"+" "*size+"|"+" "*size+"|"
