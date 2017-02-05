import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


@app.route("/swedish")
def swedish():
    # eng_words = ['fireman', 'to work', 'september', 'four', 'journalist']


    with open('static/eng_swd_vocab.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)[0:]
        print(headers[0].upper() + " ~ " + headers[1].upper())
        print('-' * 20)
        eng_words = []
        swd_words = []
        for row in reader:
            eng_word = row[0]
            swd_word = row[1]
            eng_words.append(eng_word)
            swd_words.append(swd_word)


    return render_template("swedish.html", eng_words=eng_words)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
