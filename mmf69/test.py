'''dictionary = {
	'Ricky': '1000',
	'Bobby': '1100,2200',
	'Hansel': '5000,6000,7000',
	'Mr. Burgandy': '1,2,3,4',
	'Austin': '123,4567,78,99,100',
	'Dale': '14,234,878,345,345,234'
 }
print(dictionary)'''

def sendThankYou():
    response2=input("Full Name?")
    while response2=="list":
        print(donorList.keys())
        response2=input("Full Name?")
    if not response2 in donorList:
        donorList[response2]=[]
    response3=input("Donation Amount?")
    while not response3.isdigit():
        response3=input("I'm sorry, that is not a valid number. Please try again:")
    donorList[response2].append(response3)
    print("Oh glorious "+response2+". Thank you so much for your insane gift of $" +str(response3)+"! You are truly a magnificent human!")

def createReport():
    totalDict={}
    for person in donorList:
        total,number,avg=0,0,0
        for value in donorList[person]:
            total+=int(value)
            number+=1
        avg=total/number
        totalDict[person]=[total,number,avg]
    sortedDict=sorted(totalDict.items(), key=operator.itemgetter(1))
    gridprinter(sortedDict)

def gridprinter(dict):
    size, squares,numEntries = 2,4,len(dict)
    max=maxSize(dict)
    #first element is actually number we need, not a value
    max[0]=10**max[0]
    for line in range((numEntries*2)+1):
        printedLine = ""
        if line%size==0:
            for column in range(0,squares):
                printedLine+=("+" + "-" * (len(str(max[column]))+2))
            printedLine+=("+")
        else:
            for column in range(0, squares):
                if column==0:
                    name=str(dict[int(line/size)][0])
                else:
                    pass
                    name=str(dict[int(line/size)][1][column-1])
                printedLine += ("|" + name + " " * (len(str(max[column])) + 2 - len(name)))
            printedLine+=("|")
        print(printedLine)

#Get max sizes to format grid
def maxSize(dict):
    name,total,number,avg=0,0,0,0
    for account in dict:
        total = max(total,account[1][0])
        number = max(number, account[1][1])
        avg = max(avg, account[1][2])
        name=max(len(account[0]),name)
    return [name,total,number,avg]

import operator
import random
donorList = {"Randy": [], "Erin" : [], "Lexxy": [], "Bridgette" : [], "Liz": []}
for value in donorList:
    for number in range(random.randrange(1,3)):
        donorList[value].append(random.randrange(1,1000))

while 1:
    response=input("Would you like to \"Create a report\" or \"Send a thank you\"?")
    if (response.lower()=="create a report" or response.lower()=="report"):
        createReport()
    elif (response.lower()=="send a thank you" or response.lower()=="thank you"):
        sendThankYou()
    else:
        print("That's not a valid selection. Please try again")
