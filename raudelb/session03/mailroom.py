__author__ = 'raudel'


def send_thanks(my_list):
    donors_name = []

    for i in my_list:
        donors_name.append(i[0])

    full_name = input('Please, enter the Full Name:')
    if full_name == 'list':
        print('\n----------------------------')
        print(' Donor Name')
        print('----------------------------')
        for i in my_list:
            print(i[0])
        print('-------------\n')
    elif full_name not in donors_name:
        t = (full_name, [])
        my_list.append(t)
    elif full_name in donors_name:
        donation_amount = input('Please, enter the donation amount:')
        for i in my_list:
            if i[0] == full_name:
                temp = i[1].append(int(donation_amount))
                print('Email: Thank you %s for your donation of %s $ ' % (full_name, donation_amount))
    return my_list


def create_report(my_donors):
    print('\nDonor Name\t\t|  Total Given  |  Num Gifts  |  Average Gift')
    print('---------------------------------------------------------------------')
    for i in my_donors:
        total_given = sum(i[1])
        num_gifts = len(i[1])
        avg_gift = total_given/num_gifts
        print('{0:<20s}\t $ {1:>11.2f} {2:>13}   $ {3:>12.2f}'.format(i[0], total_given, num_gifts, avg_gift))
    print('\n\n')


def main():
    list_donors = [('William Gates', [1200, 5000, 5600]), ('Mark Zuckerberg', [500, 2341]),
                   ('Jeff Bezo', [200, 423, 900, 3456]), ('Paul Allen ', [3000, 653, 45000, 2345]),
                    ('Peter Scott', [2100, 1423, 2900, 3456]), ('Paul Green ', [32000, 6253, 452000, 23425])]

    option = ''
    flag = True

    while (option != '3' or option != 3) and flag:
        print("Menu:")
        print('----------------------------')
        print('(1) Send a Thank You ')
        print('(2) Create a Report ')
        print('(3) Quit')
        print('----------------------------\n')
        option = input('Please, enter one option: ')
        if option == 1 or option == '1':
            list_donors = send_thanks(list_donors)
        elif option == 2 or option == '2':
            create_report(list_donors)
        elif option == 3 or option == '3':
            flag = False
        else:
            print('Please, enter a right option... thanks')

    print('The program has concluded..')


if __name__ == '__main__':
    main()