# in python there is no ?: operator
# this is the bes that we have


bob = True

condition = 'bob is true' if bob else 'bob is not true'

print(condition)

#tuple trick
billy = False

## (falsevalue, truevalue)
## to test change to see if condition is true or billy
tupleconditon = (5, 8)[billy] 

print(tupleconditon)

grid = [[0 for c in range(0,3)] for r in range(0,2)]

grid[0][0] = 15
grid[0][1] = 30


tupleconditon2 = (grid[0][0], grid[0][1])[billy] 

print(tupleconditon2)

