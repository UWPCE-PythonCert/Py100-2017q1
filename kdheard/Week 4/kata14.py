import random

story = ""
words = []
followup = {}
followup['s1'] = []
followup['s2'] = []
s1 = ""
s2 = ""
counter = 0

def setup(sourcetext):
    global story, words, followup, s1, s2

    with open(sourcetext, 'r') as file:
        for line in file:
            words.append(line.split(' '))
    s1 = random.choice(words)
    s2 = random.choice(words)
    print(s1)
    print(s2)

    for word in words:
        next = words.index(word)+1
        if word == s1:
            followup['s1'].append(words[next])
        if word == s2:
            followup['s2'].append(words[next])
    print(followup)
    #story_builder()


def story_builder():
    global story, words, followup, s1, s2, counter
    story = story + str(s1) + " "
    for entry in followup['s1']:
        story = story + str(entry)
    story = story + str(s2)
    for entry in followup['s2']:
        story = story + str(entry)
    story = story + "."
    sentence = ''.join(story)
    sentence[0].title()
    counter = counter + 1
    print(sentence)
    exit()





if __name__ == "__main__":
    setup('sherlock.txt')