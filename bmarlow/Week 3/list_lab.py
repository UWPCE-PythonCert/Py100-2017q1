#!/usr/bin/env python3

def main():
	l = ["Apples", "Pears","Oranges","Peaches"]
	print(l)
	l = addnewfruit(l)
	pickanumber(l)
	l = addfruittobeginningwithplus(l)
	l = addfruittobeginningwithinsert(l)
	printfruitthatstartswithP(l)

	print('The list is currently' + str(l))
	l = trimlastfruit(l)
	l = userdelfruit(l)
	#don't re-assign l for this one or it gets silly
	userdelfruitmulti(l)
	userdelwhatyoudontlike(l)
	gettingsilly(l)

def addnewfruit(l):
	new = input('Please add another fruit to the list:\n')
	l.append(new)
	print(l)
	return l

def pickanumber(l):
	num = int(input('Please enter the numeric number for the fruit you would like\n'))
	print('The number you selected is ' + str(num) + ' and the item you selected is: ' + l[num-1])

def addfruittobeginningwithplus(l):
	new = input('Please add a fruit to the beginning of the list\n')
	l = [new] + l
	print(l)
	return l

def addfruittobeginningwithinsert(l):
	new = input('Please add another fruit to the beginning of the list\n')
	l.insert(0, new)
	print(l)
	return l

def printfruitthatstartswithP(l):
	print('Printing fruits that start with \'P\'')
	for fruit in l:
		if fruit[0] == 'P':
			print(fruit)

def trimlastfruit(l):
	print('Trimming the last fruit from the list:\n')
	l = l[:-1]
	print(l)
	return l

def userdelfruit(l):
	rem = input('Please type the name of the fruit you wish to delete:\n')
	l.remove(rem)
	print(l)
	return l

def userdelfruitmulti(l):
	l = l*2
	print('Fruits have Mutated, fruits now have 2x fruits!')
	rem = input('Please type the name of the fruit you wish to delete:\n')
	for fruit in l:
		if fruit == rem:
			l.remove(fruit)
	print(l)
	return l

def userdelwhatyoudontlike(l):
	for fruit in l:
		while True:
			yn = input('do you like ' + fruit + '? (yes\\no)\n')
			if yn == 'no':
				l.remove(fruit)
				break
			elif yn == 'yes':
				break
	print(l)

def gettingsilly(l):
		newl = []
		for fruit in l:
			newl.append(fruit[::-1])
		print(newl)
		print(l)


if __name__ == '__main__':
	main()