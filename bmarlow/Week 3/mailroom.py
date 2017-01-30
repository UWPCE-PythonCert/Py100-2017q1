import os

#build our initial dictionary
dictionary = {
	'Ricky': '1000',
	'Bobby': '1100,2200',
	'Hansel': '5000,6000,7000',
	'Mr. Burgandy': '1,2,3,4',
	'Austin': '123,4567,78,99,100',
	'Dale': '14,234,878,345,345,234'
}

#we want it to be pretty, that means wiping junk off the screen
def clear():
	'''cross-platform screen clear, for prettiness'''
	os.system('cls' if os.name == 'nt' else 'clear')

#build a menu for use
def menu():
	print('Please make a selection from the menu items below\n')
	print('1.  Send a Thank You Note\n')
	print('2.  Create a report\n')
	print('Press "q" to quit\n')
	selection = input()

	if selection == '1':
		clear()
		names()
	elif selection == '2':
		clear()
		printreport()
	elif selection == 'q':
		print('exiting...')
		exit(0)
#select a name or create a new one (or list them)
def names():
	#the better way to handle this would be to use a strlower type function and compare it against strlowered names in the dictionary
	#I may add that later
	name = input('Please enter a name, or type "list" to view a list of available names (case sensitive):\n')
	clear()
	#if the name exists in our dictionary, use it
	if name in dictionary.keys():
		donations = dictionary[name]
		nameselect(name, donations)
	#you want a list of names? you got it
	elif name == 'list':
		clear()
		for key in dictionary.keys():
			print(key)
		print('')
		input('Press Enter to Continue...')
		clear()
		names()
	#you can't have a blank name silly
	elif name == '':
		clear()
		names()
	#if the name doesn't exist create it with a donation value of zero
	else:
		newname = {name : '0'}
		dictionary.update(newname)
		donations = dictionary[name]
		nameselect(name, donations)

#you have you name and the donations, lets do something with it
def nameselect(name, donations):
	newdonation = input('Please enter additional donation amount:\n')
	clear()
	donationlist = updatedonations(name, donations, newdonation)
	total = totaldonation(donationlist)
	
	printemail(name, total)

#after we take donations we want to make sure to update the dictionary
def updatedonations(name, donations, newdonation):
	#convert value string to array
	donationlist = donations.split(',')

	#if the first element is zero replace it then update the dictionary(this will math later on easier)
	if donationlist[0] == '0':
		updatedname = {name : newdonation}
		dictionary.update(updatedname)
		return newdonation
	
	#add the latest donation to the end of the array, then update the dictionary
	else:
		donationlist.append(newdonation)
		strdonationlist = ','.join(donationlist)
		updatedname = {name : strdonationlist}
		dictionary.update(updatedname)
		return strdonationlist

#print out a pretty email
def printemail(name, total):
	print('Dear ' + name +',\n')
	print('Thank you for you generous donations totalling $' + total + '.\n')
	print('Because of kind donors such as yourself we will be able to continue to provide services for years to come.\n')
	print('Sincerely,')
	print('Derek Zoolander')
	print('Director, Center for Kids Who Can\'t Read Good And Wanna Learn to do Other Stuff Good Too')
	input()
	clear()
	menu()

#convert strings to numbers, get totals, convert back to string
def totaldonation(donationlist):
	donationlist = donationlist.split(',')
	donationlist = list(map(int,donationlist))
	total = sum(donationlist)
	return str(total)	

#print a report with all of your donor information in it
def printreport():
	print('Donor Name     | Total Given | Num Gifts | Average Gift')
	print('-------------------------------------------------------')
	for name, donation in dictionary.items():
		donationlist = donation.split(',')
		donationlist = list(map(int,donationlist))
		qty = len(donationlist)
		total = sum(donationlist)
		average = round(total/qty,2)
		print("{:<16} ${:<12} {:<11} ${:<6}".format(name,total,qty,average))
	input()
	clear()
	menu()




def main():
	menu()



	


















if __name__ == '__main__':
	main()