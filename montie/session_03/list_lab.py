#!/usr/bin/env python3
print("=============Part 1===================")
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
new_fruit = input('Add a fruit, please:')
fruit_list.append(new_fruit)
print(fruit_list)
num_fruit = input('What number of fruit would you like?:')
print(fruit_list[int(num_fruit)-1])
fruit_list = ['Grapes'] + fruit_list
print(fruit_list)
fruit_list.insert(0,'rasberries')
print(fruit_list)
for a in fruit_list:
	if a[0] == 'P':
		print(a)

print("==============Part 2=================")
print(fruit_list)
del fruit_list[-1]
print(fruit_list)
del_fruit = input('Delete what fruit?')
fruit_list.remove(del_fruit)
print(fruit_list)
print("===========Part 3=================")
temp_fruit_list = fruit_list[:]
for fruit in temp_fruit_list:
	delete = input('Do you like ' + fruit + '? ')
	while delete != "no" and delete != "yes":
		delete = input('Please answer yes or no: ')
	if delete == "no":
		fruit_list.remove(fruit)
print(fruit_list)
print("==========Part 4=================")
new_fruit_list = fruit_list[:]
num = 0
for fruit in new_fruit_list:
	print(num)
	new_fruit_list[num] = fruit[::-1]
	num += 1
del fruit_list[-1]
print(fruit_list)
print(new_fruit_list)
