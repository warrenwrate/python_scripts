from time import time
import asyncio


def fib(num, mem):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if mem[num] != -1:
        return mem[num]
    else:
        return fib(num - 1, mem) + fib(num -2, mem)

num = 5
mem = [-1] * (num + 1)

fib(num, mem)
print(mem)
