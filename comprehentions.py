import os
import sys

from exseptions_ import get_insurance_amount

numbers_list = [3, 7, 70, 80, 90, -90]

target_list = []
for number in numbers_list:
    if number > 10:
        target_list.append(number * 2)
    # target_list.append(8888)

print(target_list)


target_list_2 = [number * 2 for number in numbers_list if number > 10]
# target_list_2 = {number * 2 for number in numbers_list if number > 10}
# target_list_2 = {number: number for number in numbers_list if number > 10}
# target_list_2 = {str(number): get_insurance_amount(number) for number in numbers_list}
# target_list_2 = [{number: number, 'name': 'Alex'} for number in numbers_list if number > 10]
# target_list_2 = [7777 for number in numbers_list]
print(target_list_2)
print(sys.getsizeof(target_list_2))

strange_target_list = (number * 2 for number in numbers_list if number > 10)
print(strange_target_list)
print(sys.getsizeof(strange_target_list))
# for i in strange_target_list:
#     print(i)

print(next(strange_target_list))
print(next(strange_target_list))
numbers_list.append(44)
print(next(strange_target_list))
print(next(strange_target_list))
