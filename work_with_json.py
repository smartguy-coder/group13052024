import json
from pprint import pprint

data = {
    'name': 'Alex',
    'available': False,
    'age': 15,
    'hobbies': ['soccer', 'tennis']
}

to_string = json.dumps(data)
to_string = '{"name": "Alex", "available": false, "age": 15, "hobbies": ["soccer", "tennis"]}'

# pprint(to_string)
# from_string = json.loads(to_string, parse_float=str, parse_int=int)
from_string = json.loads(to_string)
print(from_string)

with open('data.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)

with open('data.json', mode='r') as json_file2:
    data2 = json.load(json_file2)
    print(77777)
    print(data2)
