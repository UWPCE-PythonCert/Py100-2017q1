import os
import sys
import datetime
import prettytable

donors_history_file = 'donors_history.txt'
allowed_response_list = ['Send a Thank You', 'Create a Report', 'quit']


def pretty_report(header, nestedList):
    tbl = prettytable.PrettyTable(header)
    tbl.padding_width = 1
    for lst in nestedList:
        tbl.add_row(lst)
    return tbl


class File(object):
    def __init__(self, in_file):
        self.in_file = in_file

    def read_file_object(self):
        return open(self.in_file, 'r')

    def write_file_object(self):
        return open(self.in_file, 'w')

    def append_file_object(self):
        return open(self.in_file, 'a')

    def read_all_lines(self, read_object):
        return read_object.readlines()

    def close_file_object(self, in_object):
        return in_object.close()


class Prompts(object):
    def __init__(self, input_prompt):
        self.input_prompt = input_prompt

    def send_thank_you(self):
        send_thank_you_prompt = input('Enter a value: ')
        print(send_thank_you_prompt)
        if send_thank_you_prompt == 'list':
            print('In list')
            print(sorted(self.send_thank_you_list().keys()))
            self.enter_donor_amount()
        else:
            self.enter_donor_amount()

    def send_thank_you_list(self):
        donor = Donor(None)
        return donor.get_list_of_donors()

    def enter_donor_amount(self):
        response = input('Enter full name: ')
        amount = input('Enter donation amount: ')
        if response not in self.send_thank_you_list().keys():
            print('Adding {} to donors List as the name is not available'.
                  format(response))
        donor_file = File(donors_history_file)
        donor_file_a = donor_file.append_file_object()
        donor_file_a.write(response + '|' + str(amount) + '|' +
                           datetime.datetime.now().strftime('%m/%d/%Y') + '\n')
        donor_file.close_file_object(donor_file_a)
        retry_count = 0
        while retry_count < 3:
            try:
                amount = float(amount)
            except ValueError:
                print(
                    'Enter a correct amount please -- number of tries left {}'.
                    format(5 - retry_count))
                retry_count += 1
            else:
                retry_count = 5
        donor = Donor(response)
        donor.write_thank_you_letter()
        main_menu_selection()

    def create_report(self):
        report = Report('Summary')
        report.summary_report()
        main_menu_selection()


class Donor(object):
    '''all things about donor'''

    def __init__(self, donor_name):
        self.donor_name = donor_name

    @staticmethod
    def get_list_of_donors():
        donor_details_map = {}

        donor_file = File(donors_history_file)
        donor_file_r = donor_file.read_file_object()
        donor_initial_details = donor_file.read_all_lines(donor_file_r)
        donor_file.close_file_object(donor_file_r)
        for n, ln in enumerate(donor_initial_details):
            if n > 0:
                donor_details_list = ln.split('|')
                donor_name = donor_details_list[0]
                donor_amount = donor_details_list[1]
                donation_date = donor_details_list[2].strip('\n')
                value = [donor_amount, donation_date]
                if donor_name in donor_details_map.keys():
                    donor_details_map[donor_name].append(value)
                else:
                    donor_details_map[donor_name] = [value]
        return donor_details_map

    def get_donor_details(self):
        return Donor.get_list_of_donors()[self.donor_name]

    def write_thank_you_letter(self):
        donation_detail = self.get_donor_details()
        print(donation_detail)
        donor_file = './donors_letters/' + self.donor_name + '.txt'
        donor_file_object = File(donor_file)
        donor_file_object_write = donor_file_object.write_file_object()
        header = 'Donation_Date | Donation_Amount'
        line_to_be_written = 'Thank you for the generous donation - {}'.format(
            self.donor_name) + '\n'
        pretty_report = Report(None)
        pretty_table_structure = pretty_report.pretty_report(
            header.split('|'), donation_detail)
        donor_file_object_write.write(line_to_be_written)
        donor_file_object_write.write(pretty_table_structure.get_string())
        donor_file_object.close_file_object(donor_file_object_write)


class Report(object):
    '''creates the report and its objects'''

    def __init__(self, report_name):
        self.report_name = report_name

    def pretty_report(self, header, nested_list):
        tbl = prettytable.PrettyTable(header)
        tbl.padding_width = 1
        for lst in nested_list:
            tbl.add_row(lst)
        return tbl

    def summary_report(self):
        summary_list = []
        donor = Donor('Summary')
        header = 'Donor Name | Total Given | Number of Gifts | Average Gift'
        for dnr, dnr_detail in donor.get_list_of_donors().items():
            donated_amount = sum([float(x[0]) for x in dnr_detail])
            number_of_gifts = len(dnr_detail)
            summary_list.append([
                dnr, '$ ' + str(donated_amount), number_of_gifts,
                '$ ' + str(donated_amount / number_of_gifts)
            ])
        print(self.pretty_report(header.split('|'), summary_list))


def main_menu_selection():
    response = input('Choose an action from the following {}: '.format(
        allowed_response_list))
    if response == 'Send a Thank You':
        prompt = Prompts(response)
        prompt.send_thank_you()
    elif response == 'Create a Report':
        prompt = Prompts(response)
        prompt.create_report()
    elif response == 'quit':
        print('Exiting ...')
        sys.exit()


def main():
    main_menu_selection()


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
