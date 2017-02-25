#!/usr/bin/env python3
donors = ["Don Rickles","Mitch Hedberg","Dean Martin","Joan Rivers","Charles Rocket"]
donation_amount = ["50:20:100","70","491:36","10:50:71","87:92"]


def send_email(amount_donated,contributor):
	total = 0
	for num in amount_donated.split(':'):
		total += int(num)	
	print("Thank You {name} for your generous contributions.".format(name=contributor))
	print("Your most recent donation of {} is very generous and we appreciate your overall contribution of {}.".format(amount_donated.split(':')[-1],total))
	print("Sincerely, this org.")
	

def send_menu():
		send_name = input("Type in a name: ")
		if send_name == "list":
			print("\n".join(donors))
			send_menu()
		if send_name in donors:
			don_amount = input("How much did they donate? ")
			daindex = donors.index(send_name)
			if donation_amount[daindex] == "0":
				donation_amount[daindex] = don_amount
			else:
				donation_amount[daindex] = donation_amount[daindex] + ":" + don_amount
			total_donations = donation_amount[daindex]
			send_email(total_donations,send_name)
		if send_name not in donors:
			donors.append(send_name)	
			donation_amount.append("0")
			print("Not in Donor's list; added.")
			send_menu()			
		 


def create_report():
	print('{:<20s}{:<2s}{:^15s}{:<2s}{:^15s}{:<2s}{:<15s}'.format('Donor Name','|',' Total Given', '|',' Num Given','|',' Average Gift'))
	index_amount = 0
	for item in donors:
		total_amount = 0
		for num in donation_amount[index_amount].split(':'):
                	total_amount += int(num)
		num_gifts = donation_amount[index_amount].split(':')
		total_num_gifts = len(num_gifts)
		index_amount += 1
		print('{:<20s}{:>2s}{:^15.2f}{:>2s}{:^15d}{:>2s}{:^15.2f}'.format(item,'$',total_amount,' ',total_num_gifts,'$',total_amount/total_num_gifts)) 


def main_menu():
	while  True:
		print("1) Send a Thank You")
		print("2) Create a Report")
		print("3) Quit")
		main_choice = int(input("Make a selection: "))
		if main_choice == 1:
			send_menu()
		if main_choice == 2:
			create_report()
		if main_choice == 3:
			break




if __name__  == '__main__':
	main_menu()	
