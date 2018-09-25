# before list comprehension
l = []

for letter in 'word':
    l.append(letter)

print(l)

# with list comprehension
l = [ letter for letter in 'word']
print(l)

# range
lst = [ x**2 for x in range(1,5)]
print(lst)

# list comprehension
enl = [ num for num in range(0,20) if num % 2 == 0]
print(enl)

string = 'zababa'
test1 = [x for x in string if x == 'a' ]
test = ['g' if x == 'a' else x  for x in string  ]
print('only get a',test1, 'replace a with g', test)


celsius = [0,10,20,30,40]

fahrenheit = [temp * (9/5) + 32 for temp in celsius]
print(fahrenheit)

# nested list
nl = [ x**2 for x in  [ x**2 for x in range(1,5)]]
print('nested', nl)


k = [1,2,3,4,5]

n = [1,2,3]

eggfloor = [[0 for x in k] for x in n]

print(eggfloor)