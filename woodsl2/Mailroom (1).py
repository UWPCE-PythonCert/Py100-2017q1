#Mailroom

"""
AUTHOR:Lawrence Woods
FILE
NAME: mailroom.py
DATE: 3 / 20 / 17
"""
def initialize_data():
""" In this function I initializing
the data
with 5 dataet it will return the dictionary
:return:"""

data = {}  # creating dictonary
data["William Gates, III"] = [326892.24, 326892.24]
data["Mark Zuckerberg"] = [5465.37, 5465.37, 5465.37]
data["Jeff Bezos "] = [877.33]
data["Paul Allen"] = [236.14, 236.14, 236.14]
data["ravi"] = [777777.67, 888888.87]
return data


def menu():
"""
This function
prints the menu
:return:"""
print("1. Send a Thank You")
print("2. Create a Report ")
print("3. Quit")


def create_report(data_dict):
"""Creating the report of donation
:param data_dict:
:return:"""

print("{0:20}{1:20}{2:20}{3:20}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
for donor in data_dict:
    print("{0:20}  ${1:<20.2f}  {2:<20d} ${3:<20.2f}".format(donor, sum(data_dict[donor]), len(data_dict[donor]),
                                                              sum(data_dict[donor]) / len(data_dict[donor])))
print()


if __name__ == '__main__':
data = initialize_data()
while True:
    menu()
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        name = input("Enter Full Name:")
        if name == "list":
            print(data.keys())
            name = input("Enter Full Name:")
            if name not in data.keys():
                data[name] = []
            donation_amount = float(input("Enter the Donation Amount:"))
            data[name].append(donation_amount)
            print("Dear", name + ",")
            print("Thank you very much for your donation ")
    elif choice == 2:
        create_report(data)
    elif choice == 3:
        break
    else:
        print("Enter valid Input")