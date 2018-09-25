#sets are an unordered collections of unique elments.

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(1)
# should be unique
print(s)

def Set_Diff(set_x, set_y):
    return (set_x.difference(set_y))

set_A = {10, 20, 30, 40, 80}
set_B = {100, 30, 80, 40, 60}
print ('In A not in B',Set_Diff(set_A, set_B))
print ('In B not in A', Set_Diff(set_B, set_A))

#should be unique event with a list
l = [4,4,4,4,1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,]
s = set(l)
print('unique',s)

#booleans
print(1 > 2)
print(11 > 2)

b = None
print(b)

a = 'hello'
z = 'world'

print(a == z)
print(a != z)

# should be true 
print(a != z or a==z)
# should be false
print(a != z and a==z)