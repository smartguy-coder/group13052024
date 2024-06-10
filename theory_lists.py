# cities = 'Lviv Odesa     Kherson'.split()  string into list
# # result = ['Lviv', 'Odesa', 'Kherson']
#
# print(cities)
# print(cities[0])  get element of the list by index
# print(cities[2])
# # print(cities[20])
#
# odesa_name = cities[1]
# odesa_name = odesa_name.upper()
#
# cities[1] = 'Kyiv'   rewrite element
#
# cities.append(odesa_name) add one element
# cities.append(11111)
# cities.append(True)
# cities.append(None)
#
# print(len(cities))    get number of elements
# print(len('citikgjgjgghgghjjgj   gjes'))
#
# pass

new_purchase = []

mom_purchase = [
    'bread',
    'milk',
    'ice-cream',
    'water',
]

print(mom_purchase)

sister_wish = 'doll'
mom_purchase.append(sister_wish)

father_wish = [
    'beer',
    'chips',
]

# mom_purchase.append(father_wish)
# mom_purchase.extend(father_wish)             merge one list into another
#
# mom_purchase.remove('beer')  delete if exists
# # mom_purchase.remove('car')   error if not exists
# mom_purchase.pop()
# deleted = mom_purchase.pop(0)
# mom_purchase.pop(0)
# mom_purchase.insert(0, 'matches')

final_purchase_list = mom_purchase * 2   #   multiply

# new_list[0] = new_list[0] * 2
final_purchase_list[0] *= 2


number = 10
number += 5
number -= 3
number *= 3
number /= 3

final_purchase_list += father_wish
final_purchase_list += father_wish

for product_ in final_purchase_list:   # cycle
    print(product_)














