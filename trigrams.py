# -*- encode: utf-8 -*-
import io

trigrams_dict = {}

book = io.open('./data/Uncle_Sams.txt', mode='r', encoding='utf-8')
book_text = book.read(12950)
book.close()
# usable_text = book_text[2951:]


usable_text = '"We must break this up," whispered Private Hyman to Noll Terry,\
    Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'
new_text = usable_text.replace(',', '').replace('"', '')\
    .replace('.', '').replace('?', '').replace('!', '').replace('-', '')\
    .replace('\n', ' ')

print(new_text)

split_text = new_text.split(' ', 3)
print(usable_text[0:100])
print(split_text)
dict_key = split_text[0] + ' ' + split_text[1]
print(dict_key)

trigrams_dict = {}
trigrams_dict[dict_key] = []
trigrams_dict[dict_key].append(split_text[2])

print('dict: {}'.format(trigrams_dict))
