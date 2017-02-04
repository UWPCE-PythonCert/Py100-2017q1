from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return open_csv('eng_swd_vocab.csv')







def open_csv(file_path):
    """Opens a CSV file for reading."""
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)[0:]
        print(headers[0].upper() + " ~ " + headers[1].upper())
        print('-' * 20)

        score = 0
        lives = 3

        for row in reader:
            eng_word = row[0]
            swd_word = row[1]
            print("\n")
            guess = input("What is \"" + eng_word + "\" in Swedish? ")

            if guess == swd_word:
                score += 1
                print("CORRECT!")
                print("SCORE: " + str(score))
                print("LIVES REMAINING: " + str(lives))
            else:
                lives -= 1
                if lives == 0:
                    print("NOPE!")
                    print("CORRECT ANSWER: " + row[1])
                    print("SCORE: " + str(score))
                    print("*** GAME OVER ***")
                    break
                else:
                    print("NOPE!")
                    print("CORRECT ANSWER: " + row[1])
                    print("SCORE: " + str(score))
                    print("LIVES REMAINING: " + str(lives))

open_csv('eng_swd_vocab.csv')






if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
