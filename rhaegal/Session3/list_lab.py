def series2():
    fruits2=fruits[:]
    print(fruits2)
    fruits2.pop(-1)
    print("Removing the last fruit.")
    print(fruits2)
    while 1:
        response4=input("What fruit would you like to delete?")
        if response4 in fruits2:
            fruits2.remove(response4)
            print(fruits2)
            break
        else:
            print("That fruit doesn't appear in the list!")
    #bonus
    fruits2=fruits2+fruits2
    count=0
    while 1:
        response5=input("What fruit would you like to delete?")
        while response5 in fruits2:
            fruits2.remove(response5)
            count=1
        if count==1:
            break
        else:
            print("That fruit doesn't appear in the list!")
    print("Double list with "+response5+" removed:")
    print(fruits2)
    #end Series2

def series3():
    print("The original list from Series 1:")
    print(fruits)
    fruits3=fruits[:]
    for fruit in fruits3:
        while 1:
            response6=input("Do you like "+fruit.lower()+"?")
            response6=response6.lower()
            if (response6=="no" or response6=="n"):
                fruits3.remove(fruit.title())
                break
            else:
                if (response6=="yes" or response6=="y"):
                    break
                else:
                    print("yes or no please!")
    print("The list of fruits you like is:")
    print(fruits3)
    #end of Series3

def series4():
    fruits4=[]
    for fruit in fruits:
        fruits4.append(fruit[::-1])
    fruits4.pop()
    print("Original List:")
    print(fruits)
    print("Reversed List with last removed:")
    print(fruits4)
    #end of Series4

fruits=["Apples", "Pears", "Oranges", "Peaches"]

print(fruits)
response=input("Please enter a new fruit:")
fruits.append(response)
while 1:
   response2 = (input("Please enter a number between 1 and " + str(len(fruits)) + ":"))
   try:
        value=int(response2)
        if 0 < int(response2) < len(fruits):
            print("The value at index "+str(value)+" is " + str(fruits[value-1]))
            break
        else:
            print("That's not between 1 and " + str(len(fruits)) + ":")
   except ValueError:
       print("That's not a number!")
response3=[input("Please enter a new fruit:")]
fruits=response3+fruits
response4=input("Please enter a new fruit:")
fruits.insert(0,response4)
fruitsWithP=[]
for fruit in fruits:
    if fruit.startswith("P"):
        fruitsWithP.append(fruit)
print("Fruits that begin with P:")
print(fruitsWithP)
#End of Series1
series2()
series3()
series4()