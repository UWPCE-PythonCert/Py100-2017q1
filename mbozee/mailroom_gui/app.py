from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

donors = {
        'Donovan Leitch': [100.00, 20.00, 1000.00],
        'Stevie Nicks': [200.00, 500.00],
        'Suzanne Vega': [160.00, 300.00],
        'Mavis Staples': [170.00, 40.00, 130.00],
        'Ian Anderson': [190.00],
        'Eric Burdon': [207.00, 830.00, 8.00],
        'Jackson Browne': [10.00, 48.00, 1092.00, 82.00],
}


def tally_report(names, values):
    donor_name = names
    donation_total = sum(values)
    num_gifts = len(values)
    average_gift = round(donation_total / num_gifts)
    return donor_name, donation_total, num_gifts, average_gift


def print_report(donors):

    # Print each row
    for names, values in donors.items():
        donor_name, donation_total, num_gifts, average_gift = tally_report(values)

for name, amounts in donors.items():
    donor_name = name
    total_given = sum(amounts)
    num_gifts = len(amounts)
    avg_gift = round(total_given / num_gifts)

# letters = []
#
# for donor in donors:
#     letter = '''
#             Dear {},
#
#             Thank you for your generous donation of ${}.
#             Your gift makes a major impact on aspiring musicians in the Seattle area.
#
#             Sincerely,
#             Seattle Music Fund
#             '''.format(name, total_given)
#     letters.append(letter)

@app.route("/")
def index():
    '''Main view.'''

    return render_template("index.html", donors=donors)


@app.route("/", methods=['POST'])
def index_post():

    name = request.form['name']
    amount = request.form['amount']
    date = request.form['date']
    ngo = request.form['ngo']
    # donation = name + ' donated $' + amount + ' to ' + ngo + ' on ' + date + '.'

    # donors_new = dict(name=amount)
    donors[name] = [int(amount)]

    # return str(donors)
    return render_template("index.html", donors=donors)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')