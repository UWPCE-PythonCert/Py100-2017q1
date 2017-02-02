import random
def format_string(fileNumber, decimalNumber, exponentialNumber):
    print("the first 3 numbers are: file_00{:d}, {:.2f}, {:.0E}".format(fileNumber,decimalNumber,exponentialNumber))

#Not sure if you wanted this:
def format_string_infinite(*t):
    print("the first 3 numbers are: file_00{:d}, {:.2f}, {:.0E}".format(*t))

#or this:
def format_string_really_infinite(*t):
    length=len(t)
    weirdString=""+str(int(t[0]))
    num=random.randrange(1, length)
    for count in (range(1,num)):
        weirdString+=", "
        weirdString+="{:d}".format(int(t[count]))
    print("the first "+str(num)+" numbers are:" +(weirdString))

format_string(2,123.4567,200000)
format_string_infinite(2,123.4567,200000,323)
format_string_really_infinite(2, 123.4567, 200000, 323)