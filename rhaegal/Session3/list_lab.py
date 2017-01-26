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
print(fruitsWithP)

#End of Session1