import json as json_renamed

data = {
    'age': 55,
    'name': 'Василь'
}


with open('my_data.json', mode='w', encoding='utf-8') as file:
    json_renamed.dump(data, file, indent=4)
