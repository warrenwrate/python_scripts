import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379, 
    # set this so you won't have b (byte) in front of text
    charset="utf-8",
    decode_responses=True,
    db=0)


r.set('guess', ['secret', 'cool'])
r.set('lname', ('tvalue1', 'tvalue2'))

value = r.get('lname')

test = r.get('guess')


print("lname {} test{}".format(value, test))

r.delete('warrenblah')

r.lpush('warrenblah', *[1,2,3,4,5,6,7,8,9])
mlist = r.lrange('warrenblah',0,-1)

print(type(mlist))
print(mlist)

for x in mlist:
    print('number', x)


user = {"Name":"Warren", "Company":"Mill", "Address":"5th", "Location":"SEATTLE"}

r.hmset("pythonDict", user)

dictionary = r.hgetall("pythonDict")

print(dictionary)
print(value)
print(test)

name = 'myset'

r.delete(name)

r.zadd(name, 'Warren', 1)
r.zadd(name, 'bob', 2)
r.zadd(name, 'Gob', 3)
r.zadd(name, 'Parker', 4)
r.zadd(name, 'Addison', 3)
# r.zadd(name, 'Addison', 6)


print('z score test',r.zrangebyscore(name, 1, 8))
print('zrange',r.zrange(name, 0, -1, desc=True))

r.publish('events','man this even works with python!!')