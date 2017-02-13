# follow along from Treehouse Flask tutorial

import csv
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    return "Hello from {}".format(name)


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)


@app.route('/swedish')
def swd():
    with open('eng_swd_vocab.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)[0:]
        print(headers[0].upper() + " ~ " + headers[1].upper())
        print('-' * 20)
        eng_list = []
        swd_list = []
        for row in reader:
            eng_word = row[0]
            swd_word = row[1]
            eng_list.append(eng_word)
            swd_list.append(swd_word)
        return '<p>' + str(eng_list) + '</p>'

app.run(debug=True, port=8000, host='0.0.0.0')