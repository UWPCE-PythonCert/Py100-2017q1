import os
import sys
import prettytable
import datetime

maxTriesCount = 0
donors_history_file = 'donors_history.txt'


def input_prompts():
    '''
    this method prompts for the 3 values
    '''
    global maxTriesCount
    allowed_responses_list = sorted(allowed_response_map.keys())
    response = input('Choose an action from the following {}: '.format(
        allowed_responses_list))
    if str(response) not in allowed_responses_list:
        while maxTriesCount < 3:
            print(
                'Response {} is not allowed. Allowed responses are {}. Number of trials left = {}. Please try again.'.
                format(
                    str(response), allowed_responses_list,
                    str(3 - maxTriesCount)))
            maxTriesCount += 1
            input_prompts()
    else:
        allowed_response_map[response]()


def get_donors():
    '''
    this method lists the available donors
    '''
    donor_list = []
    donor_dict = {}
    try:
        with open(donors_history_file, 'r') as rF:
            next(rF)
            for ln in rF:
                ln = ln.strip('\n')
                lst = ln.split('|')
                donor_name = lst[0].strip(' ')
                donation_amt = lst[1]
                donation_date = lst[2]
                donor_list.append(lst[0])
                value = [donation_date, donation_amt]
                if donor_name in donor_dict.keys():
                    donor_dict[donor_name].append(value)
                else:
                    donor_dict[donor_name] = [value]
        return donor_dict
    except IOError as iE:
        print(iE)


def send_thank_you():
    '''
    this method is called when send thank you is selected
    '''
    response = input('Enter full name: ')
    response = response.strip(' ')
    if response == 'list':
        print('List of donors is {}'.format(get_donors().keys()))
        send_thank_you()
    else:
        enter_donor_amount(response)
        print('Available Donors are {}'.format(get_donors().keys()))
        input_prompts()


def write_thank_you_letters(response):
    '''
  this method writes individual thank you letters to disk
  '''
    donation_detail = get_donors()[response]
    file_name = './donors_letters/' + response + '.txt'
    print('Writing the thank you letter into {}'.format(file_name))
    header = 'Donation_Date | Donation_Amount'
    line_to_be_written = 'Thank you for the generous donation - {}'.format(
        response) + '\n'
    pretty_table_structure = pretty_report(header.split('|'), donation_detail)
    with open(file_name, 'w') as wF:
        wF.write(line_to_be_written)
        wF.write(pretty_table_structure.get_string())


def enter_donor_amount(response):
    '''
    this method appens amounts to the donors DS
    '''
    amount = input('Enter donation amount: ')
    if response not in get_donors().keys():
        print('Adding {} to donors List as the name is not available'.format(
            response))
    try:
        amount = float(amount)
    except ValueError:
        print('Enter a correct amount please ')
    with open(donors_history_file, 'a') as aF:
        aF.write(response + '|' + str(amount) + '|' + datetime.datetime.now()
                 .strftime('%m/%d/%Y') + '\n')
    write_thank_you_letters(response)


def quit():
    '''
    this method is called when quit is selected
    '''
    print('Exiting..')
    sys.exit()


def pretty_report(header, nestedList):
    tbl = prettytable.PrettyTable(header)
    tbl.padding_width = 1
    for lst in nestedList:
        tbl.add_row(lst)
    return tbl


def create_a_report():
    '''
    this method is called when create a report is selected
    '''
    print('Create a Report')
    summary_list = []
    header = 'Donor Name | Total Given | Number of Gifts | Average Gift'
    for dnr, dnr_detail in get_donors().items():
        donated_amount = sum([float(x[1]) for x in dnr_detail])
        number_of_gifts = len(dnr_detail)
        summary_list.append([
            dnr, '$ ' + str(donated_amount), number_of_gifts,
            '$ ' + str(donated_amount / number_of_gifts)
        ])
    print(pretty_report(header.split('|'), summary_list))
    input_prompts()


allowed_response_map = {
    'Send a Thank You': send_thank_you,
    'Create a Report': create_a_report,
    'quit': quit
}


def main():
    '''
    main method
    '''
    input_prompts()


if __name__ == '__main__':
    main()
