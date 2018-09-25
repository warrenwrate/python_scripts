
l = [
     [1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18]
     ]

print(l)
#grid to zip
a2 = zip(*l)

# row and column length
rlen = len(l)
clen = len(l[0])

print('row length', rlen, 'column length', clen)

for x, y, z in a2:
    print(x, y, z)



    



