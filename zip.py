
from random import randint as ri

xpts = [1,2,3,4]
ypts = ['w','j','a','p']
zpts = ['w','l','w','w']


zips = zip(xpts, ypts, zpts)

# print(next(zips))
# print(next(zips))


dataset = list(zips)

print('dataset',dataset)

print(ri(1,50))

d = {}
d2 = {}

#dataset [(1, 'w', 'w'), (2, 'j', 'l'), (3, 'a', 'w'), (4, 'p', 'w')]
for x, y, z in dataset:
    print(x,y,z)
    d[x] = {'fi': y, 'li': z}

print('d',d)
print('dataset 2 example')

dataset2 = [[1,'w','w'], [2,'j','w']]
for x, y, z in dataset2:
    print(x,y,z)
    d2[x] = {'fi': y, 'li': z}

print('d2',d2)

xdict = dict([[1,12],[3,4],[2,9],[3,7],[8,4]])
print(xdict)

