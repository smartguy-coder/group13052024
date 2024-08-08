def add_two_numbers(number1: int | float, number2: int | float) -> float:
    if number1 == 55:
        raise ValueError('number1 == 55')
    result = number1 + number2
    return float(result)


def add_two_numbers_bla(number1: int | float, number2: int | float) -> float:
    """according to task DEV-9867 bla-bla-bla"""
    if number1 == 0:
        return 0.0
    return add_two_numbers(number1, number2)


def multiply_by(number, by=2):
    return number * by


def get_two_time_string(number: int) -> str:
    result = str(multiply_by(number))
    return result
