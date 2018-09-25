

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


def loopyield(n):
    num = 0
    for num in range(0,n):
        yield num


for x in firstn(20):
    print(30 * x)


test = firstn(20)
test2 = loopyield(12)

print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

print(list(test))


print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))

print(list(test2))