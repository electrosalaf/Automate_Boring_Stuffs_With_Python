# pprint() and pformat() functions will “pretty print” a dictionary 

import pprint
message = 'It was a rainng day in the month of January, and the clock were stricken thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)  # setdefault() method returns the key’s value
    count[character] = count[character] + 1
       
pprint.pprint(count)
# The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

