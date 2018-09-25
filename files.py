import os
import re

#create a text file
f= open("guru99.txt","w+")

for i in range(10):
     f.writelines("This is line %d\n" % (i+1321))

warrenpath = 'c:\\Users\Warren.Wrate\\Documents\\PythonProjects\\test.txt'

x = os.path.exists(warrenpath)

print(x)

f = open(warrenpath,mode='r')

value = f.read()

print(value)

print(type(value))

#seek(0) sets the cursor to the beginning of the file
f.seek(0)
lineslist = f.readlines()



# print(lineslist)

item = re.compile(r'item|line')

#iterate through lines
for line in open(warrenpath):
    x = item.search(line)
    z = item.findall(line)
    print(z)
    if x.group() == 'item':
        print('This is an item')
    elif x.group() == 'line':
        print('this is a line')
    else:
        print('this is neither a line or item')
    # s = line[::-1]
    # print(s)

