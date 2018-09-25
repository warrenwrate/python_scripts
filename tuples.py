
#tuples are immutable
# cannot re-assign values in tuple

t = (1, 2, 1,5,6,1,6,3,3,2)
print(t)

print(len(t))

lastv = t[-1]

#count, index
t_index = t.index(5)
t_count = t.count(2)

print("Print last value: {l}, index of number 5:{index}, count:{count}".format(l = lastv, index = t_index, count = t_count))