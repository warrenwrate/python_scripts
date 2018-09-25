

#write  to file
with open('guru99.txt', 'w+') as f:
    f.write('This one is more manual\n')
    print("This is from a print statement", file=f)
    print('a','b','c','d','e', sep='*')
    f.close()

#append
with open('guru99.txt', 'a') as g:
    g.write('This should be appended\n')
    print("If not...what the heck!!", file=g)
    print('a','b','c','d','e', sep='*', file=g)

#create a new file from scratch
with open('guru98.txt', 'xt') as t:
    t.write('This one is more manual\n')
    print("This is from a print statement", file=t)
    print('a','b','c','d','e', sep='*')


#iterate over lines.
with open('guru99.txt', 'rt') as f:
    for line in f:
        print(line)