

table = [[0 for i in range(3)] for k in range(3)]

for i in range(3):
    print(table[i])

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12] 
     ]

for i in range(3):
    print(matrix[i])

print('matrix by row')
for row in matrix:
    print(row)

table2 = [[row[i] for row in matrix] for i in range(4)]

print('table 2')
for i in range(4):
    print(table2[i])

transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])

for i in range(4):
    print(transposed[i])