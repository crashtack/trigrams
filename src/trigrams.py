# -*- encode: utf-8 -*-
import io
import sys


def trigrams(path, num_words):
    path = '../data/Uncle_Sams.txt'

    trigrams_dict = {}

    try:
        # do_something()
        book = io.open(path, mode='r', encoding='utf-8')
        book_text = book.read(12950)
        book.close()
        # f = open('missing.txt')
        # process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

    # usable_text = book_text[2951:]

    usable_text = '"We must break this up," whispered Private Hyman to Noll Terry,\
        Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'
    new_text = usable_text.replace(',', '').replace('"', '')\
        .replace('.', '').replace('?', '').replace('!', '').replace('-', '')\
        .replace('\n', ' ').replace('(', '').replace(')', '').replace(';', '')
    new_text = new_text.lower()

    index = 0

    words = new_text.split()
    print(words)
    print()
    print('removing spaces')

    print()
    for index, word in enumerate(words):
        if index <= len(words) - 3:
            dict_key = words[index] + ' ' + words[index + 1]
            # print(dict_key)
            trigrams_dict.setdefault(dict_key, []).append(words[index + 2])
            # trigrams_dict
            # if dict_key not in trigrams_dict:
            #     trigrams_dict[dict_key] = [words[index + 2]]
            # else:
            #     trigrams_dict[dict_key].append(words[index + 2])

    for key in trigrams_dict:
        print('{:<20}\t{}'.format(key, trigrams_dict[key]))
        # print('dict: {}'.format(trigrams_dict))

    # "{0} {1}".format(*my_tuple[:2])     # use this structure, it's pythonic

    # return choice(my_dict[key])    # returns random element from array in key
    #

    # trigram_dict.setdefault(dect_key[]).append(dect_value)




def main():
    USAGE = '''
Usage: trigrams <input path> <words> > <ouput path>

Example: trigrams some_book.txt 500 > my_output.txt
'''

    if len(sys.argv) != 3:
        print(USAGE)
        sys.exit(1)

    try:
        # trigrams(str(sys.argv[1]), int(sys.argv[2]))
        print(sys.argv[0])
        print(sys.argv[1])
        print(sys.argv[2])
    except RuntimeError:
        print("This is a generic error, i'm still figuring this out")

if __name__ == '__main__':
    main()
