# # list
# from copy import copy, deepcopy
# from sys import getsizeof
#
# new_list = list()
# new_list2 = [3]
# new_list3 = ['string', 2, 3.0, True, False, None, new_list2, print]
# print(new_list3)
#
# new_list2.append(5555)
#
# print(id(new_list3))
# new_list3.append(444)
# print(id(new_list3))
# print(new_list3)
#
#
# # new_iterator_4 = iter(new_list3)
# # print(f'{getsizeof(new_list3)=}')
# # print(f'{getsizeof(new_iterator_4)=}')
# #
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # new_list3.append(55)
# # new_list3.append(56)
# # new_list3.append(57)
# #
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
# # print(next(new_iterator_4))
#
#
# print(new_list3)
# print('8'*99)
# # for element in new_list3:
# #     print(element)
# #     # new_list3.append(7)
# #     new_list3.pop()
#
#
#
# #
# #
# #
# # n = 5
# # print(id(n))
# # n += 1
# # print(id(n))
#
#
# # def foo(data: list = []) -> list:
# #     data.append(2)
# #     print(data)
# #     return data
#
#
# def foo(data: list = None) -> list:
#     if not data:
#         return [2]
#     data.append(2)
#     print(data)
#     return data
#
# # print(foo([]))
# # print(foo([55]))
# # print(foo([]))
# # print(foo([]))
# # print(foo([]))
# # foo()
# # foo()
#
#
#
# n = 5
# m = n
#
# print(n)
# print(m)
# print(id(n))
# print(id(m))
# n = 700
# print(n)
# print(m)
# print(id(n))
# print(id(m))
#
# lst4 = new_list3
# lst4.append(77787877)
# print(new_list3)
#
# # copy
# # 1
# print(1111111111111111)
# # for element in copy(new_list3):
# # for element in deepcopy(new_list3):
# #     print(element)
# #     new_list2.append(67)
# #     # new_list3.append(7)
# #     new_list3.pop()
# #     print(new_list3)
#
# print(883838838383883838383838838383838388)
# # list_slice = new_list3[:]
# list_slice = new_list3[::-2]
#
# string = 'asdfghjkl'[::-1]
# print(string)
#
#
# # new_list2.append(67)
# # list_slice.append(8888)
# # print(id(new_list3))
# # print(id(list_slice))
# print(list_slice)
# # print(new_list3)
# #
# #
# # for element in new_list3:
# #     print(element)
# #     new_list2.append(67)
# #     # new_list3.append(7)
# #     new_list3.pop()
# #     print(new_list3)
#




# set
# new_set = set()
# new_set1 = {}
# # new_set2 = {3, 6, True, 77, []}
#
# list1 = [1, 2, 1, 'fff']
# set_from_list = set(list1)


# list_from_set = list(set_from_list)
# set_from_string = set('gfjegfgkjsfgkh22sdhjf      gkjdsfggjhdsfgjdfkgdjg')
# list_from_string = list('gfjegfgkjsfgkh22sdhjfgkjds     fggjhdsfgjdfkgdjg')
#
# print(set_from_list)
# print(set_from_string)
# print(list_from_string)
# print(list_from_set)
# list_from_set.append([])
# print(list_from_set)
# for i in set_from_list:
#     print(i)


set1 = {
    1,
    2,
    3,
}

set2 = {3, 4, 5}

# common elements
common1 = set1.intersection(set2)
common2 = set1 & set2

print(f'{common1=} {2+2=}')
print(f'{common2=}')

# union all elements
all_elem1 = set1.union(set2)
all_elem2 = set1 | set2
print(f'{all_elem1=}')
print(f'{all_elem2=}')

# difference
diff = set1 - set2
print(f'{diff=}')

# all diff
total_diff = set1 ^ set2
print(f'{total_diff=}')




# dict revision

dict1 = {'name': "alex", 'weight': 67}
dict2 = {'age': 13,  'weight': 34 }

# all_together = {**dict1, **dict2}
all_together = dict1 | dict2
print(all_together)

# dict1.update(dict2)

print()
























# my_tuple = 44, 66, 77, 888
# print(my_tuple)
# print(set1)
#
# print(type(set2))












