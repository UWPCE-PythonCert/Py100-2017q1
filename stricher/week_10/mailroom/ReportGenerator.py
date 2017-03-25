
from TextGenerator import TextGenerator

class ReportGenerator(TextGenerator):

    def __init__(self):
        super(ReportGenerator, self).__init__()


class ReportDonationsDBGenerator(ReportGenerator):

    from Database import Database

    def __init__(self, donations_db: Database):
        self.__db = donations_db
        super(ReportDonationsDBGenerator, self).__init__()

    def _generate(self) -> str:
        donors_id = self.__db.donations_table.get_donors_id_sorted_per_total_hist_donation_amount()

        total_donation_per_donor = self.__db.donations_table.get_total_donations_amounts()
        num_donations_per_donor = self.__db.donations_table.get_num_gifts()
        avge_donation_per_donor = self.__db.donations_table.get_average_gift()

        string = "\nList of donors:\n\n"
        string += 99 * '*' + '\n'
        string += '{:^20}'.format('PersonName') + '|'\
                  + '{:^30}'.format('Total amount') + '|' \
                  + '{:^25}'.format('Number of donations') + '|' \
                  + '{:^20}'.format('Average donation') + '|'\
                  + '\n'
        string += 99 * '*' + '\n'
        ii = 0
        for don_id in donors_id:
            string += "" if ii == 0 else "\n"
            name = str(self.__db.donors_table.get_donor_name(don_id))
            string += '{:20}'.format(name) + '|'
            string += '{:>30.2f}'.format(total_donation_per_donor[don_id]) + '|'
            string += '{:>25}'.format(num_donations_per_donor[don_id]) + '|'
            string += '{:>20.2f}'.format(avge_donation_per_donor[don_id]) + '|'
            ii += 1
        string += '\n'
        string += 99 * '*' + '\n'
        return string

