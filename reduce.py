import functools
 
# initializing list
lis = [ 4 , 3, 5, 6, 2 ]
 
# using reduce to compute sum of list
print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))
 
# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

print ("The minimum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a < b else b,lis))

print ("count")
print (functools.reduce(lambda a,b: a+1,lis))

print(lis)

def f(x): return x % 3 == 0 or x % 5 == 0


fil = list(filter(f, range(2, 25)))

print(fil)

def cube(x): return x*x*x


map_cube = map(cube, range(1, 11))

ml = list(map_cube)

print(ml)