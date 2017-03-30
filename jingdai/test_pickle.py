def conver_to_roman(a,map):

    a=int(a)
    if a==0:
        print("Roman number does not include Zero.")
    else:
        if a/10<1:
            return map[a]
        if a/10>=1 and a/10<10:
            pass




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
print(map1)




#map1={10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",16:"XVI",17:"XVII",18:"XVIII",19:"XIX"}
#map2={20:"XX",21:"XXI",22:"XXII"}
#user_input = input("number>>")
#b=conver_to_roman(user_input,map)
#print(b)
