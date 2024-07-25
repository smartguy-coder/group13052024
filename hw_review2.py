def dec(func):

    def wrapper(*args, **kwargs):
        result = {}
        res = func(*args, **kwargs)
        result.update({'result': res})
        print(f"{result=}")
        return result

    return wrapper


@dec
def foo1():
    return 777

@dec
def foo2():
    return 77778687


@dec
def foo3():
    return 77778687797977


res_foo1 = foo1()
print(res_foo1)

res_foo1[66] = 9898989889
print(res_foo1)

foo2()
