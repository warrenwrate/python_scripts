import time as t

# begint = t.time()
# t.sleep(5)
# endt = t.time()
# print(endt - begint + 1)

beginTest = t.time() 

#add 20 seconds
endt = beginTest + 20

while beginTest < endt:
    t.sleep(4)
    print('just a test')
    beginTest = t.time()

print('All done')