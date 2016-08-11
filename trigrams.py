# -*- encode: utf-8 -*-
import io
from string import maketrans

book = io.open('./data/Uncle_Sams.txt', mode='r', encoding='utf-8')
book_text = book.read(12950)
book.close()
usable_text = book_text[2951:]

# inrep  = u',.?!"-'
# outrep = u'      '
#
# tranrep = maketrans(inrep, outrep)
# new_text = usable_text.translate(tranrep)

# print(new_text)

usable_text = '"We must break this up," whispered Private Hyman to Noll Terry,\
    Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'
new_text = usable_text.replace(',', '').replace('"', '')\
    .replace('.', '').replace('?', '').replace('!', '').replace('-', '')\
    .replace('\n', ' ')

print(new_text)

# split_text = new_text.split(' ', 2)
# print(usable_text[0:100])

# dict_key = split_text[0] + ' ' + split_text[1]

# print(dict_key)
