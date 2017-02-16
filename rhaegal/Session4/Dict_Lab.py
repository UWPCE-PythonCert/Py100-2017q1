dict = {'Name': "Chris", 'city': "Seattle", 'cake': "Chocolate"}
print(dict)
dict.pop('cake', None)
print(dict)
dict['fruit']="Mango"
print(dict.keys())
print(dict.values())
if "cake" in dict:
    print("Cake is in the dict!")
else:
    print("Cake is not in the dict.")
if "Mango" in dict.values():
    print("Mango is in the dict!")
else:
    print("Mango is not in the dict.")

#End of series1
dict2={}
for x in dict:
    dict2[x]="t"
s2,s3,s4=set(),set(),set()
s2.update(range(0,20,2))
s3.update(range(0,20,3))
s4.update(range(0,20,4))
print(s2)
print(s3)
print(s4)

def subset(sub, super):
    for val in sub:
        if not val in super:
            return(False)
    return(True)

print(subset(s3,s2))
print(subset(s4,s2))

s5=set()
for char in "Python":
    s5.update(char)
s5.update('i')
s6=frozenset(['m','a','r','a','t','h','o','n'])
print(s5.union(s6))
print(s5.intersection(s6))