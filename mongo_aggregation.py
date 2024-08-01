import datetime
from pprint import pprint
from uuid import uuid4

from pymongo.mongo_client import MongoClient
from bson import Decimal128

from config import USER_NAME, PASSWORD

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster13052024.8tqgq8d.mongodb.net/?retryWrites=true&w=majority&appName=cluster13052024"

# Create a new client and connect to the server
client = MongoClient(uri)

# db = client.test_db
db = client['new_db']

prod_coll = db['products']


products = [
    {
        'title': 'bread with nuts',
        'price': 100,
        'remains': 66,
        'comment': 'no sugar',
        'contain_gluten': True,
        'date': datetime.datetime.utcnow(),
    },
    # {
    #     'title': 'soft drink',
    #     'price': 24,
    #     'remains': 2787,
    #     'comment': 'really sweet',
    #     'contain_gluten': True,
    #     'date': datetime.datetime(year=2024, month=8, day=10, hour=5),
    # },
    # {
    #     'title': 'milk',
    #     'price': 45,
    #     'remains': 565,
    #     'comment': 'natural',
    #     'contain_gluten': False,
    #     'date': datetime.datetime.now() - datetime.timedelta(days=1),
    # },
    # {
    #     'title': 'vinegar',
    #     'price': 15,
    #     'remains': 55,
    #     'comment': 'apple taste',
    #     'contain_gluten': False,
    #     'date': datetime.datetime.now() + datetime.timedelta(hours=56),
    # },
]

# prod_coll.insert_many(products)

# analog search

# query = []
# response = prod_coll.aggregate(query)
# pprint(list(response))

# match stage
query = [
    {'$match': {'contain_gluten': False}}
]
query = [
    {'$match': {
        # '$and': [
        '$or': [
            {'contain_gluten': True},
            {'price': {'$gte': 40}},
        ]
        }
    }
]
response = prod_coll.aggregate(query)
pprint(list(response))
