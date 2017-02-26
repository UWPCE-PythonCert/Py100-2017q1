#!/usr/bin/env python3

class Arabic_Number (object):
    def __init__(self):
        numbers=[]

    def print_numbers(self):
        numbers=[0,1,2,3,4,5,6,7,8,9]
        return numbers

    def convert_to_Roman(self):

        user_input=input("give me a Arabic number less than 100: >>")
        user_input=int(user_input)
        map={0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        map1={}
        for key in map:
            map1[key]=map[key]
            map1[key+10]="X"+map[key]
            map1[key+20]="XX"+map[key]
            map1[key+30]="XXX"+map[key]
            map1[key+40]="XL"+map[key]
            map1[key+50]="L"+map[key]
            map1[key+60]="LX"+map[key]
            map1[key+70]="LXX"+map[key]
            map1[key+80]="LXXX"+map[key]
            map1[key+90]="XC"+map[key]
        if user_input==0:
            print("Roman number does not include Zero.")
        else:
            return map1[user_input]




class Roman_Number (object):
    def __init__(self):
        symbol={}

    def convert_to_Arabic(self):
        user_input=input("give me a Roman number less than One Hundred: >>")
        map={0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        map1={}
        map2={}
        for key in map:
            map1[key]=map[key]
            map1[key+10]="X"+map[key]
            map1[key+20]="XX"+map[key]
            map1[key+30]="XXX"+map[key]
            map1[key+40]="XL"+map[key]
            map1[key+50]="L"+map[key]
            map1[key+60]="LX"+map[key]
            map1[key+70]="LXX"+map[key]
            map1[key+80]="LXXX"+map[key]
            map1[key+90]="XC"+map[key]
        map2 = {y:x for x,y in map1.items()} # switch the key and value
        return map2[user_input]




if __name__ == "__main__":
    number=Arabic_Number()
    number.print_numbers()
    b=number.convert_to_Roman()
    print("The converted Roman Number is: {}".format(b))

    symbol=Roman_Number()
    c=symbol.convert_to_Arabic()
    print("The converted Arabic Number is: {}".format(c))

