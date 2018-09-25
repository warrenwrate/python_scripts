

dictionary = [
    {
        'id': 1,
        'name': 'Warren',
        'city': 'Redmond',
        'state': 'WA',  
    },
        {
        'id': 2,
        'name': 'Addison',
        'city': 'Redmond',
        'state': 'WA',  
    },
        {
            
        'id': 3,
        'name': 'Parker',
        'city': 'Redmond',
        'state': 'WA',  
    }

]

new_dictionary = { x['name']: x for x in dictionary}

print(new_dictionary['Addison'])

print(new_dictionary.get('Bob', {'message': 'member cannot be found'}))

print(new_dictionary.get('Bob', {'message': None}))


print('new dictionary\n',new_dictionary)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))

print(d)

my_list = ['hello', 'hi', 'memory', 'hello', 'memory', 'mommy', 'hello']
f_letter = [x[0] for x in my_list]
my_dict = {k:my_list.count(k) for k in my_list} #
fl_dict = {k[0]:f_letter.count(k[0]) for k in f_letter} 
print('word count', my_dict)
print('first letter dictionary', fl_dict)

new_d ={}

#long way for above
for l in my_list:
    h = new_d.get(l, None)
    if h:
        new_d[l] += 1
    else:
        new_d[l] = 1

print(new_d)