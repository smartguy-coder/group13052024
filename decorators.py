from typing import Callable

database = {
    'login': '123',
    'password': '123'
}

def log_decorator(filename='log.csv'):
    def _log_decorator(func: Callable):
        def wrapper(*args, **kwargs):
            print(1111)
            result = func(*args, **kwargs)
            print(2222)

            with open(filename, mode='a', encoding='utf-8') as log_file:
                log_file.write(f'{func.__name__};{result};{args};{kwargs}\n')
            # if result == 'bentley':
            #     send_email()
            return result

        # wrapper.__name__ = func.__name__
        return wrapper

    return _log_decorator


def auth_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print(33333)
        login = input('Enter_login')
        password = input('Enter_password')
        if login == database['login'] and password == database['password']:
            result = func(*args, **kwargs)
        else:
            raise ValueError('Who are you?')
        print(44444)
        return result
    return wrapper


@auth_decorator
@log_decorator(filename='another.csv')
def add_two_numbers(number_one: int, number_two: int) -> int:
    result = number_one + number_two
    print(555555555555)
    return result


add_two_numbers(2, 7)


def divide_two(number_one: int, number_two: int) -> float:
    result = number_one / number_two

    return result


@log_decorator()
def add_the_numbers(number_one: int, number_two: int, third_number: float) -> float:
    result = number_one + number_two + third_number
    return result


add_the_numbers(1, 2, 3)


# print(foo)
# print(type(foo))
# print(type(55))
# print(foo.__code__)
# print(foo.__dict__)
# foo.age = 55
# print(foo.__dict__)

# new_func = foo
#
# print(new_func)
# print(foo)
#
# n = print
#
# n(878686778)
# print(n)


# lst = [2, 3, 77, 7877, 888]
# # lst = [2, 3]
# first, second, *other = lst
# print(first)
# print(second)
# print(*other)  # 77, 7877, 888
# print(77, 7877, 888)  # 77, 7877, 888


# def wrapper(func: Callable, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     result = func(*args,  **kwargs)
#     return result
#
#
# # result = wrapper(add_two_numbers, 2, 6)
# # result = wrapper(add_two_numbers, number_two=88, number_one=77)
# result = wrapper(add_two_numbers, 88, sep=77)
# print(result)
#
#
# add_two_numbers(number_two=88, number_one=77)


# add_two_numbers = simple_decorator(func=add_two_numbers)
# divide_two = simple_decorator(func=divide_two)
#
# print(add_two_numbers.__name__)
#
# res = add_two_numbers(4, 5)
# res = divide_two(4, 5)
# print(res)
