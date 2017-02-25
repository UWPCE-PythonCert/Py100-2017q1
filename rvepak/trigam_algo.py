import sys
word_dict = {}
word_list = []
processed_words = {}
gln = ''


def create_list():
    with open('sample.txt', 'r') as rF:
        for ln in rF:
            ln = ln.replace('--', ' ')
            ln = ln.replace(',', '')
            ln = ln.replace('.', '')
            ln = ln.strip('\r\n')
            lst = ln.split(' ')
            for y in lst:
                word_list.append(y)
    print(word_list)


def create_dict():
    for n in range(len(word_list)):
        try:
            key = word_list[n] + ' ' + word_list[n + 1]
            value = word_list[n + 2]
            if key in word_dict.keys():
                word_dict[key].append(value)
            else:
                word_dict[key] = [value]
        except:
            pass
    print(word_dict)


def concatenate_all_values(val):
    global gln
    gln = gln + ' ' + val


def func_return_value(key, cnt):
    try:

        if key in processed_words.keys():
            processed_words[key] += 1
        else:
            processed_words[key] = 0
        try:
            recurValue = word_dict[key][processed_words[key]]
        except Exception:
            recurValue = word_dict[key][0]
        recursKey = key.split(' ')[1] + ' ' + recurValue
        if cnt == 0:
            concatenate_all_values(key + ' ' + recurValue)
        else:
            concatenate_all_values(recurValue)
        cnt += 1
        func_return_value(recursKey, cnt)
    except KeyError as kE:
        pass

    #return


def main():
    create_list()
    create_dict()
    k = func_return_value('I may', 0)
    print(gln)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

#print(gln)
