class Donor:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.donations = []

    def add_donation(self, amount):
        self.donations.append(amount)

    def mean_donation(self):
        from statistics import mean
        return mean(self.donations)

    def sum_donation(self):
        return sum(self.donations)

    def number_of_donations(self):
        return len(self.donations)

    def print_donor_contributions(self):
        print("{} {}".format(self.first_name, self.last_name).ljust(26), end='')
        print("$%12.2f" % self.sum_donation(), end='')
        print("%12d  " % self.number_of_donations(), end='')
        print("$%12.2f" % self.mean_donation())

    def get_donor_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __lt__(self, other):
        return self.mean_donation() < other.mean_donation()

    def __gt__(self, other):
        return self.mean_donation() > other.mean_donation()
