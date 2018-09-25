
import pickle

a = [1,2]
b = [3,4]

values = list()
values.append(a)
values.append(b)

pkldump = pickle.dumps(values)

j, k = pickle.loads(pkldump)
print('value of j {}, value of k{}'.format(j, k))

with open("tmp.pkl", "wb") as f:
    pickle.dump(values, f) # pickle.dump([a,b], f) or pickle.dump((a,b), f) will work as well.

with open("tmp.pkl", "rb") as f:
    a,b = pickle.load(f) 

print('a data', a)
print('b data', b)


d = {}

# d[1001] = {
#     'name': 'warren',
#     'address': '123 Baker Street',
#     'friend': 'watson',
#     'pet': None
# }

d= {
    1001:{
        'name': 'warren',
        'address': '123 Baker Street',
        'friend': 'watson',
        'pet': None
    }
}

print(d[1001]['name'])