my_dict = {'firstname': 'Warren', 'lastname': 'Wrate'}

post = {"author": "Warren",
               "text": "Parker is my buddy",
               "tags": ["bulk", "insert"],
               "day": 28}

print(post['day'])

my_value = my_dict['firstname']

print(my_value)

d = {}

d['animal'] = 'dog'
d['crazy'] = True

d['name'] = {'dogFirstName': 'Rover', 'origin':{'country': 'England'}}

print(d['name']['dogFirstName'])
print(d['name']['origin']['country'])

print(d.keys())
print(d.values())
print(d.items())

l = ['bob', 'animal', 'crazy', 'name']

for i in l:
    if i in d:
        print('is a key')
    else:
        print('is not a key')

names = {}
names['warren'] = 'value for Warren'

def checkname(name):
    if names.get(name):
        print("I found you " + name)
    else:
        print('Could not find ' + name)


checkname('warren')


print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345

for i in d :
    print("%s  %d" %(i, d[i]))