import asyncio
from time import time

hashmap = {}

async def foo():
    print('Running in foo')
    await asyncio.sleep(5)
    if 5 in hashmap:
        hashmap[5] +=10
    print(hashmap[5])
    print('Ended foo')


async def bar():
    print('Running bar')
    hashmap[5] = 10
    await asyncio.sleep(2)
    print('Ended Bar')


async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)

start = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time()
print('time ran in', end - start,'seconds')
