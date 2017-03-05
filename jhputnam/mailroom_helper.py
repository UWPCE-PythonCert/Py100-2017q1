#!/usr/bin/env python3

"""Mailroom class."""

from operator import itemgetter


class MailRoom:
    """Mailroom class object."""

    def __init__(self, donors):
        """Init class with instance vars unique to each instance."""

        # Set variables used by various class methods.
        self.donors = donors

    def add_donation(self, donorname, donation):
        """
        Method to handle adding donations to the donor dict.

        Args:
            donorname: Full name of the donor.
            donation: Donation amount.

        Returns:
            A dictionary object containing donors.
        """

        if donorname not in self.donors:
            print("The name \'{}\' is not in the donor database. Adding name"
                  " as a new donor.\n".format(donorname))
            self.donors[donorname] = [donation]
        else:
            print("The name \'{}\' was found in the donor database. Adding new"
                  " donation.\n".format(donorname))
            self.donors[donorname].append(donation)

        return self.donors

    @staticmethod
    def _sum_report(values):
        """
        Static method to tally donations for report generation.

        Args:
            values: List containing donation amounts for each donor.
        """

        donation_total = sum(values)
        num_gifts = len(values)
        average_gift = donation_total / num_gifts

        return donation_total, num_gifts, average_gift

    def generate_report(self):
        """
        Method to genereate a report sorted by donation amount.
        """

        print()
        print("     NAME            TOTAL          NUMBER       AVERAGE ")
        print("----------------------------------------------------------")

        for name, value in sorted(self.donors.items(), key=itemgetter(1),
                                  reverse=True):

            (donation_total, donations,
             average) = MailRoom._sum_report(value)

            print("{:<20} ${:<15.2f} {:<8} ${:<0.2f}".format(name,
                                                             donation_total,
                                                             donations,
                                                             average))
