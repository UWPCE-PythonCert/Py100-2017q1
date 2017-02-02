#!/usr/bin/env python3

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# list1=['Apples', 'Pears', 'Oranges','Peaches']
# print(list1)
# # Ask the user for another fruit and add it to the end of the list.
# user_input=input('what''s your favorite fruit? > ')
# list1.append(user_input)
# print(list1)
# # Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
# user_input1=input('give me a number in the range of 0 to 5 > ')
# print(list1[int(user_input1)])
# #Add another fruit to the beginning of the list using “+” and display the list.
# list1=['Grapefruit']+list1
# print(list1)
# #Add another fruit to the beginning of the list using insert() and display the list.
# list1.insert(0,'Papaya')
# print(list1)
# # Display all the fruits that begin with “P”, using a for loop.
# for fruit in list1:
#     if fruit[0]=='P':
#         print(fruit)
#
# # Display the list.
# # Remove the last fruit from the list.
# list1.pop()
# print(list1)
# # Display the list.
# # Ask the user for a fruit to delete and find it and delete it.
# user_input2=input('What do you want to delete? > ')
# list1.remove(user_input2)
# print(list1)
# # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
# list1.extend(list1)
# print(list1)
#list1=['Papaya', 'Grapefruit', 'Apples','Pears', 'Oranges', 'Peaches', 'Papaya', 'Apples','Grapefruit', 'Pears', 'Oranges', 'Peaches']
# user_input3=input("Which fruit to delete? > ")
# for fruit in list1:
#     if fruit ==user_input3:
#         list1.remove(user_input3)
# print(list1)

# Ask the user for input displaying a line like “Do you like apples?”
#user_input4=input("do you like apples? > ")

# for each fruit in the list (making the fruit all lowercase).
# list2=[]
# for fruit in list1:
#     fruit=fruit.lower()
#     list2.append(fruit)

# print(list2)
# list2.remove("apples")
# print(list2)

# For each “no”, delete that fruit from the list.
# if user_input4=='no':
#     for fruit in list2:
#         if fruit ==("apples"):
#             list2.remove(fruit)
# print(list2)

# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
# Display the list.

# while True:
#     if user_input4 not in ("yes","no"):
#         print("please provide a yes or no as an answer. bye. ")
#         break


# Make a copy of the list and reverse the letters in each fruit in the copy.
list1=['Papaya', 'Grapefruit', 'Apples','Pears', 'Oranges', 'Peaches']
list2=[]
l=len(list1)
for i in range(1,l+1):
    list2.append(list1[l-i])
    i=i+1
print(list2)

# Delete the last item of the original list. Display the original list and the copy.
list1.pop()
print(list1)
print(list2)



