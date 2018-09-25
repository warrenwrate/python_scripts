import pymongo as pym
from bson.objectid import ObjectId
import datetime
from random import randint

client = pym.MongoClient()

d = client.database_names()

print(d)

db = client['wwTest520']

c = db.collection_names()

print(c)
# collection = db['firstcollection']
coll = db.firstcollection

# coll.delete_one({'_id': ObjectId("5a6a476e1663610af43bbf65")})

data = coll.find_one

print('data',data)

print('type:',type(data))

#for loop
monglist = []
for datta in coll.find():
    monglist.append(datta)
    print('info',datta['info'])
    #print(datta['_id'].generation_time)

# count of documents
print("length of documents %d" %(len(monglist)))

print(monglist[3])


db_posts = client['Posts']
coll_posts = db_posts['collPosts']

print("\n\nPrinting Other DBs")


for post_data in coll_posts.find({'author': 'Warren'}):
    print('post data:', post_data)
    print('generation time:', post_data['_id'].generation_time)
    try:
        #coll_posts.delete_one({'_id': ObjectId(post_data['_id'])})
        print('deleted:',post_data['author'])
        print("\n")
    except Exception as e:
        print('error:', e)

dt  = datetime.datetime(2018, 11, 10, 10, 45)
print(str(dt))


start = datetime.datetime(2018, 11, 7, 10, 45)
end = datetime.datetime(2018, 11, 15, 10, 45)

x = coll_posts.find_one( {'date': {'$lt': end, '$gte': start}})
print('\nDataFound')
print(x)



# coll_posts.delete_one({'_id': ObjectId("5a6a520216636130ecfe110a")})
# coll_posts.delete_one({'_id': ObjectId("5a6a520216636130ecfe110b")})


new_posts = [{"author": "Warren",
               'randomNo': randint(0,90),
               "text": "Parker is my buddy",
               "tags": ["bulk", "insert"],
               "date": dt},
              {"author": "Jessica Wrate",
               'randomNo': randint(0,90),
               "title": "Just another test",
               "text": "parenting is stressful",
               "date": dt}]

result = coll_posts.insert_many(new_posts)
# new_ids = result.inserted_ids

# print(new_ids)
