import random

def main(sourcetext):
    words = []
    document = open(sourcetext, 'r')
    for word in document:
        words.append(word)
    s1 = random.choice(words)
    s2 = random.choice(words)
    followup = {}
    followup['s1'] = []
    followup['s2'] = []

    #TODO get the words before and after s1 and s2, add to acceptable_words dict


if __name__ == "__main__":
    main('sherlock_small.txt')