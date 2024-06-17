# from pprint import pprint
#
# person_name = 'Alex'
# person_age = 16
#
# person = {
#     'name': 'Alex',
#     'age': 16,
#     'hobbies': [
#         'soccer',
#         'tennis',
#     ],
#     'address': None,
# }
#
# address = person.get('address', 777) or 'Odesa'
# print(address)
#
# shipment = {}
# shipment['phone'] = 'iPhoneX'
# shipment['plate'] = 'from Ukraine with love'
# shipment['plate1'] = 'from Ukraine with love2222'
# shipment['plate2'] = 'from Ukraine with love'
# shipment['plate4'] = 'from Ukraine with love'
# shipment['plater'] = 'from Ukraine with love'
# shipment['weather'] = 'cloudy'
# shipment['weather'] = 'sunny'
# shipment[5] = 'sunny'
# shipment[5.0] = 'sunny3'
#
#
# pprint(shipment, indent=4)
#
#
# # item_from_shipment = shipment['phone']
# #
# # item_from_shipment = shipment[5]
# # item_from_shipment = shipment.get('5')
# # print(item_from_shipment)
# # item_from_shipment = shipment.get('5', 'something')
#
# # print(item_from_shipment)
#
# del shipment[5]
#
# value = shipment.pop('plate1', )
# print(value)
# shipment.pop('plate1', 555)
#
#
# shipment['plate2'] = 'plate2'
# shipment['plate1'] = 'from Ukraine with love2222'
#
# pprint(shipment, indent=4)
# print(shipment)
#


cars = [
    {
        'number': 1,
        'color': 'black',
        'price': 120.5,
        'features': [
            'jump',
        ]
    },
    {
        'number': 3,
        'color': 'black',
        'price': 1200.5,
        'features': [
            'radio',
            'retro',
        ]
    },
    {
        'number': 11,
        'color': 'white',
        'price': 100.5,
        'made in': 'China',
        'in_sale': True,
        'empty': None
    },
]


# for car in cars:
#     print(f'price  {car["price"]}')
#     for feature in car.get("features", []):
#         print(feature)
#     print('~' * 20)

my_tuple = 3, 77
print(my_tuple)

value1, value2 = my_tuple

person = {'name': 'Alex', 'age': 16, 'hobbies': ['soccer', 'tennis',], 'address': None}
print(person.items())
# for item in person:
#     print(item)
#     print(person[item])
#     print('~' * 20)
for key, value in person.items():
    print(key, '>>>',  value)
    # print(person[item])
    print('~' * 20)


for key in person.keys():
    print(key)
    print('+' * 20)

for value in person.values():
    print(value)
    print('=' * 20)