import asyncio  
import time  
from datetime import datetime


async def factorial(name, number):
    print('Task {} started!!'.format(name))  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await asyncio.sleep(1)
        f += i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))


start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(factorial("A", 20)),
    asyncio.ensure_future(factorial("B", 9)),
    asyncio.ensure_future(factorial("C", 18)),
    asyncio.ensure_future(factorial("D", 5))
]

loop.run_until_complete(asyncio.wait(tasks)) 

print("hello world")
#loop.run_until_complete(tasks) 
loop.close()

end = time.time()  
print("Total time: {}".format(end - start))
