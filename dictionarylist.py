


post = {"author": "Warren",
         "text": "Parker is my buddy",
         "tags": ["bulk", "insert","Transfer", 'Eat', "Export", "Import"],
         "day": 28,
         "month": 1,
         "year": 2017}

post2 = {"author": "Warren",
         "text": "Addison is my is my buddy",
         "tags": ["bulk", "insert","Transfer", 'Eat', "Export", "Import"],
         "day": 28}


p = {"author": "Warren",
         "text": "Parker is my buddy",
         "day": 28,
         "month": 1,
         "year": 2017}

p2 = {"author": "Warren",
         "text": "Addison is my is my buddy",
         "day": 28}

l = ["bulk", "insert","Transform",  "Export", "Import"]

for t in post['tags']:
    if t in l:
        print("%s could be found" %t)
    else:
        print("ERROR: %s could not be found" %t)

# set of keys in common
j = post.keys() & post2.keys()
# set of different keys (in post but not in post2)
k = post.keys() - post2.keys()
# key and item is th same.  Though will not work if any items in the dictionary are lists or dicts
i = p.items() & p.items()
print(j)
print(type(j))

print(k)
print(type(k))

print(i)
print(type(i))

lis = list(j)

print(lis)
print(type(lis))
