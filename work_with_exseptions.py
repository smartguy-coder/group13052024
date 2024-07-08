from exseptions_ import get_insurance_amount


class InsuranceAmountError(Exception):
    pass


def divide_two_numbers(*, divisible: int, divisor: int) -> float:
    try:
        share = divisible / divisor
        if not share:
            raise ValueError
        get_insurance_amount(share)
    except ZeroDivisionError as e:
        print(e)
        raise
    except (TypeError, ValueError):
        share = 2.0
    else:
        print(888888)
    finally:
        print(9999999)
        share = 99.00

    return share


print(divide_two_numbers(divisible=90, divisor=0))
