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
        new_pair=(user_prompt1,float(user_prompt2))
        donation.append(new_pair)
    else:
        new_pair1 = (user_prompt1,0)
        donation.append(new_pair1)
        names.append(user_prompt1)

    for name in names:
        print("Dear {}, thank you for your generous donation.".format(name))



def create_a_report(donation):
    names=[]
    for pair in donation:
        if pair[0] not in names:
            names.append(pair[0])

    sum_lists=[]
    for i in names:
        sum=0
        count=0
        for j in donation:
            if i==j[0]:
                sum=j[1]+sum
                count=1+count
        sum_list=(i,sum,count,float(sum/count))
        sum_lists.append(sum_list)


    header_line='{:>12}  |{:>12}  |{:>12}  |{:>12}  '.format("Donor Name","Total Given","Num Gifts","Average Gift")
    print(header_line)
    for sum_list in sum_lists:
        line_new = '{:>12}  ${:>12}  {:>12}  ${:>12}  '.format(*sum_list)
        print(line_new)
    return

if __name__ == "__main__":
    donation=[("Andy",300),("Sally", 400),("Andy",100),("Tom",700),("Lisa",90),("Abby",1000),("Abby",200)]
    while True:
        user_prompt=input("1.Send a Thank You; 2.Create a Report; 3.quit > ")

        if user_prompt=="2":
            create_a_report(donation)
        if user_prompt=="1":
            send_a_thankyou(donation)
        if user_prompt=="3":
            print("goodbye")
            break





