#!/usr/bin/env python3

dict1={'name':'Chris','city':'Seattle','cake':'chocolate'}
print(dict1)
dict1.pop('cake')
print(dict1)
dict2={'fruit':'mango'}
dict1.update(dict2)
print(dict1)
print(dict1.keys())
print(dict1.values())
print('cake'in dict1)
if 'mango' in dict1.values():
    print('True')
else:
    print("False")

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value. (upper and lower case?).
dict4={}
dict3={}

for key in dict1:
    count=0
    for i in dict1[key].lower():
        if i=='t':
            count=count+1
    dict3={key:count}
    dict4.update(dict3)
print(dict4)

s2=set()
s3=set()
s4=set()

for i in range(21):
    if i%2==0:
        s2.update([i])
    if i%3==0:
        s3.update([i])
    if i%4==0:
        s4.update([i])
print(s2)
print(s3)
print(s4)

print(s2.issubset(s3))
print(s4.issubset(s2))

s5=set('Python')
s6=set('i')
s5.update(s6)
print(s5)

s7=frozenset('marathon')
print(s7)
print(s5.union(s7))
print(s5.intersection(s7))

