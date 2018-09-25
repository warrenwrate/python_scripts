## nice handy dandy tip

size = 3

trav = [[0 for c in range(0,size)] for r in range(0,size)]

track = 0

for i in range(0,size):
    for j in range(0,size):
        if i + j < size:
            print('row', j, 'col', i +j)
    
    if track < size:
        track += 1