__author__ = 'raudel'
import re


def clean_up_document(doc):
    my_doc = re.split('[^a-zA-Z]', doc)
    l = len(my_doc) - 1
    for i in range(l, 0, -1):
        if len(my_doc[i]) == 0:
            del my_doc[i]
    return my_doc


def create_token_list(doc_list):
    value_list = []
    my_dic = dict()
    j = 0
    l = len(doc_list)
    for i in range(l-2):
        temp_key = doc_list[i]+' ' + doc_list[i+1]
        if not (temp_key in my_dic):
            temp_list = list()
            temp_list.append(doc_list[i+2])
            my_dic[temp_key] = temp_list
        else:
            temp_value = my_dic[temp_key]
            temp_value.append(doc_list[i+2])
            my_dic[temp_key] = temp_value

    return my_dic


def generate_text(key_text, t_list, my_string):
    if key_text in t_list:

        if not len(my_string):
            my_string = key_text

        list_values = t_list[key_text]

        while len(list_values):
            value = list_values[0]

            if len(list_values) > 1:
                del t_list[key_text][0]

            my_string += ' ' + value
            temp_list = my_string.split()
            key_text = temp_list[-2] + ' ' + temp_list[-1]

            return generate_text(key_text, t_list, my_string)
    else:
        return my_string


def main():
    f = open('sherlock_small.txt')
    text = f.read()
    doc_list = clean_up_document(text)

    token_list = create_token_list(doc_list)

    print(token_list)
    print('--------------')
    my_text = input("Please, enter the text key with two words (recomended: his hands): ")

    if my_text in token_list:
        my_str = ''
        text_generated = generate_text(my_text, token_list, my_str)
        print('The text generated is: ', text_generated)
    else:
        print('This key is not valid..')

    f.close()


if __name__ == '__main__':
    main()
