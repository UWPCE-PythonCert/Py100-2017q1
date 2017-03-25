
#

'''
1)return a sequence with the first and last items exchanged.
'''

def a():
temp1 = "asdfgt"
temp2 = list(temp1)
temp2[0],temp2[-1]=temp2[-1],temp2[0]
temp1 = ''.join(temp2)
return temp1
str=a()
print(str)


'''
2) return a sequence with every other item removed
'''

def a():
a = [123, 234, 345];
n=len(a)
item=123
for i in range(0,n-1):
if(a[i]!=123):
a.remove(a[i])
a.remove(a[n-2])
return a


str=a()
print(str)


'''
3) return a sequence with the first and last 4 items removed, and every other item in between
    return a sequence reversed (just with slicing)
'''
def a():
a = [123, 234, 345,56,78,67,45,34,34,56,78];
n=len(a)
a.remove(a[0])
a.remove(a[n-2])
a.remove(a[n-3])
a.remove(a[n-4])
a.remove(a[n-5])
item=123
new = a[::-1]
return new


str=a()
print(str)


'''
4)return a sequence with the middle third, then last third, then the first third in the new order
'''


def a():
    str = [1, 2, 3, 4, 5, 2, 3, 5, 672, 6, 4, 23, 4]


n = len(str)
str1 = str[0:2]
str2 = str[n - 5:n - 2]
str3 = str[n / 2 - 1:n / 2 + 1]

str.remove(str[0])
str.remove(str[1])
str.remove(str[2])
str4 = str2 + str;
str4.remove(str4[n / 2])
str4.remove(str4[n / 2 + 1])
str4.remove(str4[n / 2 - 1])
str5 = str4[:n / 2]
str5 = str5 + str3
n1 = len(str5)
str5.remove(str5[n1 - 2])
str5.remove(str5[n1 - 3])
str5.remove(str5[n1 - 4])
str6 = str5 + str1
return str6

str23 = a()
print(str23)



