#!/usr/bin/env python3
import random

book_file = "./sherlock.txt"
# book_file = "./sherlock_small.txt"


word_pairs = {}


def read_book():
    with open(book_file, 'r') as f:
        book_text = f.read().replace('\n', ' ')
    book_text = book_text.replace('.', '')
    book_text = book_text.replace(',', '')
    book_text = book_text.replace('"', '')
    book_text = book_text.replace('!', '')
    book_text = book_text.replace('?', '')
    book_text = book_text.replace('  ', ' ')
    book_text = book_text.replace('  ', ' ')
    book_text = book_text.replace("'", '')
    book_text = book_text.replace("(", '')
    book_text = book_text.replace(")", '')
    book_text = book_text.replace(";", '')
    book_text = book_text.replace("-", '')
    return book_text


def generate_word_pairs(param):
    book_text = param.split()
    for i in range(len(book_text) - 3):
        key = " ".join(book_text[i:i + 2])
        value = book_text[i + 2]
        # print(key +' '+ value)
        if key in word_pairs:
            word_pairs[key].append(value)
        else:
            word_pairs[key] = [value]
            # print(word_pairs)


def add_sentence():
    start_key = random.choice(list(word_pairs.keys()))
    new_sentence = start_key
    while start_key in word_pairs:
        new_sentence += " " + random.choice(word_pairs[start_key])
        start_key = new_sentence.split()
        start_key = (' '.join(start_key[-2:]))
    return new_sentence + "."


def write_new_book():
    new_book = ""
    i = 1
    while i <= 1:
        new_book += str(add_sentence())
        i += 1
    print(new_book)


if __name__ == '__main__':
    book_text = read_book()
    generate_word_pairs(book_text)
    write_new_book()
