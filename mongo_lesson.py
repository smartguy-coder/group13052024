from pprint import pprint
from uuid import uuid4

from pymongo.mongo_client import MongoClient

from config import USER_NAME, PASSWORD

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster13052024.8tqgq8d.mongodb.net/?retryWrites=true&w=majority&appName=cluster13052024"

# Create a new client and connect to the server
client = MongoClient(uri)

# db = client.test_db
db = client['new_db']

mops_coll = db['mops']
crayons_coll = db['crayons']

# CREATE
# insert single document
# mops_coll.insert_one({'title': 'Super mop', 'price': 8888, 'uuid': str(uuid4())})
# crayons_coll.insert_one({'title': 'purple one', 'price': 20})

# insert many docs

docs = [
    {'title': 'Super mop', 'price': 500, 'uuid': str(uuid4()), 'features': ['clean', 'fresh']},
    {'title': 'Super mop6', 'price': 666, 'uuid': str(uuid4())},
    {'title': 'Super mop', 'price': 555, 'uuid': str(uuid4())},
    {'title': 'Super mop', 'price': 200, 'uuid': str(uuid4())},
]
mops_coll.insert_many(docs)

# READ DATA
# first

# result = mops_coll.find_one()
# print(result)

# result = mops_coll.find_one({'uuid': '020d46d7-79b3-481d-bcdc-9c4ec27e12e6'})
# print(result)
#
# result = mops_coll.find_one({'price': 200, 'year': 2222})
# print(result)

# find many
# result = list(mops_coll.find())
# result = mops_coll.find()
# for doc in result:
#     pprint(doc)

# query = {'price': 200}
# result = mops_coll.find(query)
# pprint(list(result))

query = {'price': {'$gt': 200, '$lt': 400}}
query = {'price': {'$gt': 200}}
query = {'price': {'$gte': 200, '$lte': 400}}
query = {
    'price': {'$gte': 200, '$lte': 400},
    'title': 'Super-puper mop'
}
query = {
    'price': {'$gte': 200, '$lte': 400},
    'title': {'$regex': 'Su*'}
}
result = mops_coll.find(query).limit(4).sort('price', -1).skip(2)
pprint(list(result))