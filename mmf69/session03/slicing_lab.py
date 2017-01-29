'''------------------------------------------------------------------------------------------------
Slicing Lab
return a sequence with the first and last items exchanged.
return a sequence with every other item removed
return a sequence with the first and last 4 items removed, and every other item in between
return a sequence reversed (just with slicing)
return a sequence with the middle third, then last third, then the first third in the new order
-----------------------------------------------------------------------------------------------'''

s =  "What is that dog's name?"
print(s)
print(len(s))

#return a sequence with the first and last items exchanged.
print(s[23] + s[1:22]  + s[0])

#return a sequence with every other item removed
print(s[::2])

#return a sequence reversed (just with slicing)return a sequence reversed (just with slicing)
print(str(s[::-1]))

#return a sequence with the middle third, then last third, then the first third in the new order



