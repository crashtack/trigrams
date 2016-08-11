# -*- encode: utf-8 -*-
import io

trigrams_dict = {}

book = io.open('./data/Uncle_Sams.txt', mode='r', encoding='utf-8')
book_text = book.read(12950)
book.close()
usable_text = book_text[2951:]


# usable_text = '"We must break this up," whispered Private Hyman to Noll Terry,\
    # Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'
new_text = usable_text.replace(',', '').replace('"', '')\
    .replace('.', '').replace('?', '').replace('!', '').replace('-', '')\
    .replace('\n', ' ').replace('(', '').replace(')', '').replace(';', '')
new_text = new_text.lower()

# print(new_text)

index = 0

words = new_text.split(' ')
# print(words)
while words.count(''):
    words.remove('')
print()
print('removing spaces')
# print(words)
print()
for index, word in enumerate(words):
    if index <= len(words) - 3:
        dict_key = words[index] + ' ' + words[index + 1]
        # print(dict_key)
        if dict_key not in trigrams_dict:
            trigrams_dict[dict_key] = [words[index + 2]]
        else:
            trigrams_dict[dict_key].append(words[index + 2])

for key in trigrams_dict:
    print('{:<20}\t{}'.format(key, trigrams_dict[key]))
    # print('dict: {}'.format(trigrams_dict))
