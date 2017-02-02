def switchFirstLast(str="A sample test string"):
    return str[-1:] + str[1:-1] + str[0:1]

def everyOther(str="A sample test string"):
    return str[::2]

def firstLastFour(str="A sample test string"):
    return str[4:-4]

def reverse(str="A sample test string"):
    return str[::-1]

def middleLastFirstThird(str="A sample test string"):
    offset=len(str)%3
    step=int(len(str)/3)
    return str[step+(offset>0):2*step+offset]+str[2*step+offset:] + str[:step+(offset>0)]

print(switchFirstLast())
print(everyOther())
print(firstLastFour())
print(reverse())
print(middleLastFirstThird())