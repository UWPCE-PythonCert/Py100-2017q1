from flask import Flask, render_template, flash, request, url_for

app = Flask(__name__)


class Donor:
    '''Donor stuff.'''
    def __init__(self, donors, donors_sorted, donor_name, total_given, num_gifts, avg_gift):
        self.donors = donors
        self.donors_sorted = donors_sorted
        self.donor_name = donor_name
        self.total_given = total_given
        self.num_gifts = num_gifts
        self.avg_gift = avg_gift

    donors = {
        'Donovan Leitch': [100.00, 20.00, 1000.00],
        'Stevie Nicks': [200.00, 500.00],
        'Suzanne Vega': [160.00, 300.00],
        'Mavis Staples': [170.00, 40.00, 130.00],
        'Ian Anderson': [190.00],
        'Eric Burdon': [207.00, 830.00, 8.00],
        'Jackson Browne': [10.00, 48.00, 1092.00, 82.00],
    }

    for name, amounts in donors.items():
        donor_name = name
        total_given = sum(amounts)
        num_gifts = len(amounts)
        avg_gift = round(total_given / num_gifts)

    # def sort_donors(self):
    #     '''Maintain order of donors dict.'''
    #     self.donors_sorted = sorted(self.donors.items(),
    #                            key=lambda t: sum(t[1]), reverse=True)
    #
    #     for donor in self.donors_sorted:
    #         self.donor_name = donor[0]
    #         self.total_given = sum(donor[1])
    #         self.num_gifts = len(donor[1])
    #         self.avg_gift = round(sum(donor[1]) / len(donor[1]))
    #
    #     return self.donors_sorted


@app.route("/", methods=['GET', 'POST'])
def index():
    '''Main view.'''

    return render_template("index.html", donors=Donor.donors, donor_name=Donor.donor_name)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')