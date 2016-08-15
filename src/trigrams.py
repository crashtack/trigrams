# -*- encode: utf-8 -*-
import io
import sys
from copy import deepcopy
from random import choice


def trigrams(book_text, num_words):
    trigrams_dict = {}

    usable_text = book_text[2951:]

    # usable_text = '"We must break this up," whispered Private Hyman to Noll Terry,\
        # Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'

    new_text = remove_punctuation(usable_text)

    words = new_text.split()

    for index, word in enumerate(words):
        if index <= len(words) - 3:
            dict_key = words[index] + ' ' + words[index + 1]

            # setdefault creates a new key pair if it does not exist
            # else it updates an existing key pair
            trigrams_dict.setdefault(dict_key, []).append(words[index + 2])

    # for key in trigrams_dict:
    #     print('{:<20}\t{}'.format(key, trigrams_dict[key]))

    new_text = get_fisrt_3_words(trigrams_dict)

    for i in range(num_words - 2):
        key = get_next_key(new_text)
        new_text += ' ' + get_next_word(trigrams_dict, key)

    print('{}'.format(new_text))

    # some notes i took
    # "{0} {1}".format(*my_tuple[:2])     # use this structure, it's pythonic
    # return choice(my_dict[key])    # returns random element from array in key
    # sum(1.0 / (i * 3 + 1) for i in range(n))
    # trigram_dict.setdefault(dect_key[]).append(dect_value)


def get_fisrt_3_words(d):
    ''' returns the first 3 words of the story '''
    key_dict = deepcopy(d)
    key = key_dict.popitem()
    # print('the key: {}'.format(key))
    # print(type(key))
    # print('{}'.format(key[0]) + ' {}'.format(choice(key[1])))
    return '{}'.format(key[0]) + ' {}'.format(choice(key[1]))


def get_next_key(s):
    words = s.split()
    # print('get key: {}'.format(words[-2]) + ' {}'.format(words[-1]))
    return '{}'.format(words[-2]) + ' {}'.format(words[-1])


def get_next_word(trigrams_dict, k):
    # print('get next word key: {}'.format(k))
    # print('next word: {}'.format(choice(trigrams_dict[k])))
    return choice(trigrams_dict[k])


def remove_punctuation(text):
    ''' Removes punctuation except '
        TODO: refactor this, it looks ugly to me '''
    new_text = text.replace(',', ' ').replace('"', '')\
        .replace('.', '').replace('?', ' ').replace('!', ' ')\
        .replace('\n', ' ').replace('(', '').replace(')', '')\
        .replace(';', ' ').replace('-', ' ')
    new_text = new_text.lower()
    return new_text


def load_file(path):
    # path = '../data/Uncle_Sams.txt'
    try:
        book = io.open(path, mode='r', encoding='utf-8')
        book_text = book.read(12950)
        book.close()
        return book_text
    except IOError:
        print("couldn't open {}".format(path))


def main():
    USAGE = '''
Usage: trigrams <input path> <words> > <ouput path>

Example: trigrams some_book.txt 500 > my_output.txt
'''

    if len(sys.argv) != 3:
        print(USAGE)
        sys.exit(1)

    try:
        book_text = load_file(sys.argv[1])
        trigrams(book_text, int(sys.argv[2]))
    except RuntimeError:
        print("This is a generic error, i'm still figuring this out")

if __name__ == '__main__':
    main()
