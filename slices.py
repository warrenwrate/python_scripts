

#using named slices to grab data.

record = '10212     53001012018Warren       Wrate'

emp_id = slice(0,5)
amount = slice(10,13)
date = slice(13,21)
fname = slice(21,34)
lname = slice(34,40)

print(record[emp_id])
print(record[amount])
print(record[date])
print(record[fname].rstrip())
print(record[lname])