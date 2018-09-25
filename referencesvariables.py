

hello = 'hello'

h = hello

h += 'a'

print(h)
print(hello)

#reference pointer to objects
# this works because list is an object
a = [1,2,3,4,5,6,7]
print('a',a)
b = a
b.append(8)
print('b',b)
print('a',a)


## to make them separate use copy

c = a.copy()
c.append(9)
print('using copy to create a separate memory bank')
print('c:',c)
print('a:',a)
print('b:',b)



# main point to this is objects keep their refence while decorators do not
# this is why this name change works when the other didn't above.
class Name():

    def __init__(self):
        self.name = 'bob'

class Test():

    def __init__(self):
        self.name = Name()
    
    def namechange(self):
        fname = self.name
        fname.name += ' Wrate'
        return fname

t = Test()
print(t.name.name)
print(t.namechange().name)
print(t.name.name)
        