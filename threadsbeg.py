from threading import Thread
from time import time, sleep


def test(i, j, sl):
    print('number:', i, "started")
    sleep(sl)
    print('values', i, j)
    

t1 = Thread(target=test, args=[1, 2, 4])
t2 = Thread(target=test, args=[2, 5, 8])
t1.start()
t2.start()
print('hello')



