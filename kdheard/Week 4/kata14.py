def main(sourcetext):
    words = []
    s1 = []
    s2 = []
    acceptable_words = {}
    acceptable_words['s1'] = []
    acceptable_words['s2'] = []
    for word in sourcetext:
        words.append(word)

    #TODO find out how to split out individual words from sourcetext
    #TODO select random word from words
    #TODO get the words before and after s1 and s2, add to acceptable_words dict


if __name__ == "__main__":
    main('sherlock_small.txt')