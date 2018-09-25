

from itertools import groupby


things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

#tells the group by to use the first value as the grouping key
#shows complete grouping
for key, group in groupby(things, lambda x: x[0]):
    print('this is the group by key', key,list(group),'\n')

#splits out by group
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print( "A %s is a %s." % (thing[1], key))
    print(" ")

# Place data into a Dictionary
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
d = {}
for key, group in groupby(things, lambda x: x[0]):
    d[key] = []
    for thing in group:
        d[key].append(thing[1])

print(d)


thinglst = [["animal", "bear"], ["animal", "duck"], ["plant", "cactus"], ["vehicle", "speed boat"], ["vehicle", "school bus"]]

#tells the group by to use the first value as the grouping key
#shows complete grouping
for key, group in groupby(thinglst, lambda x: x[0]):
    print('this is the group by key', key,list(group),'\n')
