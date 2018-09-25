from itertools import combinations

combolist = combinations([0,1,2,7,6], 3) 

print(combolist.__next__())
print(next(combolist))
print(next(combolist))
print(next(combolist))
print(next(combolist))
print(next(combolist))
print(next(combolist))

print(list(combolist))