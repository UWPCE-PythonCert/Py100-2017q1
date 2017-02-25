#!/usr/bin/env python3
#Learn basic Python list io
#http://uwpce-pythoncert.github.io/IntroToPython/exercises/list_lab.html#exercise-list-lab


fruit = [ "Apples", "Pears", "Oranges", "Peaches" ]
print("The current list contains",len(fruit),"fruit:", fruit)

response = input("Which fruit would you like to append to the list? ")
fruit.append(response)
print("The current list contains",len(fruit),"fruit:", fruit)

response = int(input("Please select a particular fruit by providing a number: "))
print("The", response, "fruit is ", fruit[response-1])

fruit = ["Mandarins"] + fruit
print("The current list contains",len(fruit),"fruit:", fruit)

fruit.insert(1, "Pineapples")
print("The current list contains",len(fruit),"fruit:", fruit)

print("Fruits in the list that begin with 'P': ")
for i in range(len(fruit)):
    if fruit[i][0] == "P": print(fruit[i])

print("The current list contains",len(fruit),"fruit:", fruit)
fruit.remove(fruit[-1])
print("The current list contains",len(fruit),"fruit:", fruit)

response = input("Which fruit would you like to delete from the list? ")
if response in fruit:
        fruit.remove(response)
print("The current list contains",len(fruit),"fruit:", fruit)

print("The current list contains",len(fruit),"fruit:", fruit)
fruit = fruit * 2
print("The current list contains",len(fruit),"fruit:", fruit)

response = []
while (response not in fruit):
    try:
        response = input("Which fruit would you like to delete from the list? ")
    except ValueError:
        print("Fruit not in list")
        continue
    else:
        break

while (response in fruit):
    fruit.remove(response)
print("The current list contains",len(fruit),"fruit:", fruit)

fruit = [ "Apples", "Pears", "Oranges", "Peaches" ]
fave_fruit = []
for i in fruit:
    print("Do you like",i.lower(),"?")
    response = input()
    while response not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'")
        response = input()
        continue
    if response == 'yes':
        fave_fruit.append(i)

print("The current list contains",len(fave_fruit),"fruit:", fave_fruit)

fruit = [ "Apples", "Pears", "Oranges", "Peaches" ]
fruit_c = []
for i in fruit:
    fruit_c.append(i[::-1])
fruit.remove(fruit[-1])
print("The current list contains",len(fruit),"fruit:", fruit)
print("The current copy contains",len(fruit_c),"fruit:", fruit_c)
