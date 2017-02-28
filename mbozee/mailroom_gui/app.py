from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    '''Main view.'''
    donors = {
        'Donovan Leitch': [100.00, 20.00, 1000.00],
        'Stevie Nicks': [200.00, 500.00],
        'Suzanne Vega': [160.00, 300.00],
        'Mavis Staples': [170.00, 40.00, 130.00],
        'Ian Anderson': [190.00],
        'Eric Burdon': [207.00, 830.00, 8.00],
        'Jackson Browne': [10.00, 48.00, 1092.00, 82.00],
    }

    donors_sorted = sorted(donors.items(),
                           key=lambda t: sum(t[1]), reverse=True)

    for donor in donors_sorted:
        donor_name = donor[0]
        total_given = sum(donor[1])
        num_gifts = len(donor[1])
        avg_gift = round(sum(donor[1]) / len(donor[1]))

    return render_template("index.html", donors=donors, donors_sorted=donors_sorted, donor_name=donor_name, total_given=total_given, num_gifts=num_gifts, avg_gift=avg_gift)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')