#!/usr/bin/env python3

def send_a_thankyou(donation):

    user_prompt1=input("type List or a name > ")

    if user_prompt1=='List':
        print(donation)
        return
#     If the user types a name not in the list, add that name to the data structure and use it.
# create a name list
    names=[]
    for pair in donation:
        if pair[0] not in names:
            names.append(pair[0])
#print(name)

    if user_prompt1 in names:
        user_prompt2=input("Amount > ")
        try:
            user_prompt2<0
        except:
            print('Please enter a positive number')
        new_pair=(user_prompt1,float(user_prompt2))
        donation.append(new_pair)
    else:
        new_pair1 = (user_prompt1,0)
        donation.append(new_pair1)
        names.append(user_prompt1)

    #for name in names:
    print("Dear {}, thank you for your generous donation.".format(user_prompt1))



def create_a_report(donation):
    names=[]
    for pair in donation:
        if pair[0] + pair[1] not in names:
            name=pair[0]+pair[1]
            names.append(name)

    sum_lists=[]
    for i in names:
        sum=0
        count=0
        for j in donation:
            if i==j[0]+j[1]:
                sum=j[2]+sum
                count=1+count
        sum_list=(i,sum,count,float(sum/count))
        sum_lists.append(sum_list)
    print(sum_lists)

    header_line='{:>12}  |{:>12}  |{:>12}  |{:>12}  '.format("Donor Name","Total Given","Num Gifts","Average Gift")
    print(header_line)
    for sum_list in sum_lists:
        line_new = '{:>12}  ${:>12}  {:>12}  ${:+.2f}  '.format(*sum_list)
        print(line_new)
    return sum_lists

def send_a_letter(donation):
    names=[] #create a list which has all the donor's name
    for pair in donation:
        if (pair[0],pair[1]) not in names:
            name=(pair[0],pair[1])
            names.append(name)

    sum_lists=[] # create a list which has donor's name and the sum donation amount.
    for i,z in names:
        sum=0
        for j in donation:
            if (i,z)== (j[0],j[1]):
                sum=j[2]+sum
                sum_list=(j[0],j[1],sum)
        sum_lists.append(sum_list)

    list_of_dict=[] # create a list of dictionary which contains donor's first and last name and the sum donation amount.
    dict={}
    for donate in sum_lists:
        dict["First_Name"]=donate[0]
        dict["Last_Name"]=donate[1]
        dict["Amount"]=donate[2]
        list_of_dict.append(dict.copy())
    for i in list_of_dict:
        print("Dear {First_Name} {Last_Name}, \n Thank you so much for your donation of {Amount} dollars. \n We wish you a happy 2017!".format(**i))



if __name__ == "__main__":
    donation=[("Andy","Thomas", 300),("Sally", "Bui", 400),("Andy","Tom", 100),("Tom","Colin", 700),("Lisa","Dodo",90),("Abby","Lust",1000),("Abby","Lust",200)]
    while True: #while loop if input value not in the defined value, it just go back to the first input.
        user_prompt=input("1.Send a Thank You; 2.Create a Report; 3.Send a Letter; 4.quit > ")
        if user_prompt not in '1234':
            print("Please select a number that is in the range of 1 to 4.")

        if user_prompt=="2":
            create_a_report(donation)
        if user_prompt=="1":
            send_a_thankyou(donation)
        if user_prompt=="3":
            send_a_letter(donation)
        if user_prompt=="4":
            print("goodbye")
            break





