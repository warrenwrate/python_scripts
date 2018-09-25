from functools import reduce


#method parameter
def methodparam(param):
    return param()

def addnum():
    return 30 + 5

n = methodparam(addnum)

print(n)

print(methodparam(lambda: 20 + 32))

mlist = [1,2,3,4,5,6]

#filter
print(list(filter(lambda x: x !=3, mlist)))

def odd(x):
    if x % 2 == 1:
        return x

print(list(filter(odd, mlist)))


#map
values = [1, 2, 3, 4, 5]

def mymap(x):
    if x % 2 == 1:
        x *= 10
    else:
        x *= 100
    return x

# Note: We convert the returned map object to
# a list data structure.
add_10 = list(map(lambda x: x + 10, values))
add_20 = list(map(lambda x: x + 20, values))

map_fun = list(map(mymap, values))

print("Map Function")
print(add_10)
print(add_20)
print(map_fun)


from functools import reduce

values = [1, 20, 3, 40, 5]

print("Reduce Function")
summed = reduce(lambda a, b: a + b, values)
mult = reduce(lambda a, b: a * b, values)

checkadd = reduce(lambda a, b: a + b if( a + b < 40) else a + 0, values)
print(summed)
print(mult)
print(checkadd)
#>> 10
