#yield returns a generator ( like range) to only be iterated once

l = [1,2,4,6,2,1,51,2,38,5,1,51,851,3,58,4,24]

# example 1
print('example 1')
def dedup(items): 
    s = set()   
    for i in items:
        if i not in s:
            yield i
            s.add(i)

for d in dedup(l):
    print(d)

#example 2
print("\nexample 2")
def gen():
    for x in range(10):
        yield x

for g in gen():
    print(g * 2)