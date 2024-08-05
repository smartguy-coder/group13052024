# l = [1]
#
# for el in l:
#     l.append('f')
#     print(el)
limit = 888
var = 0

# while var < limit:
#     var += 5
#     print(var)

# flag = True
# while flag:
#     var += 5
#     print(var)
#     if var > limit:
#         flag = False

# while True:
#     var += 5
#     print(var)
#     if var > limit:
#         break




def get_user_age() -> int:
    while True:
        candidate = input('Enter your age, number >>> ')
        if candidate.strip().isdigit() and int(candidate.strip()) > 0:
            return int(candidate.strip())
        else:
            print('Enter correct data')







print(get_user_age())












