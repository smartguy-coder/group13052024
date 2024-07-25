result = {}


def dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        result.update({'result': res})
        print(f"{result=}")
        return result

    return wrapper


result[3] = 88

@dec
def foo1():
    return 777

@dec
def foo2():
    return 77778687


@dec
def foo3():
    return 77778687797977


foo1()
print(result)

foo2()
print(result)