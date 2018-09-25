

words = ['hello', 'world']

_end = '_end_'

#short hand
root = dict()
for word in words:
    current_dict = root
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end

#longhand
troot = dict()
for word in words:
    current_dict = troot
    for letter in word:
        current_dict[letter] = {}
        current_dict = current_dict[letter]
        #current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end

print(troot)

#{'w': {'o': {'r': {'l': {'d': {'_end_': '_end_'}}}}}, 'h': {'e': {'l': {'l': {'o': {'_end_': '_end_'}}}}}}
#{'w': {'o': {'r': {'l': {'d': {'_end_': '_end_'}}}}}, 'h': {'e': {'l': {'l': {'o': {'_end_': '_end_'}}}}}}