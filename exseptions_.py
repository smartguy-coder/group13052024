RATE = 20


class InsuranceAmountError(Exception):
    pass


def calculate_life_insurance():
    raise NotImplementedError


def get_insurance_amount(car_price: int | float) -> float:
    if car_price < 0:
        # raise Exception('Too low cost')
        # raise ValueError('Too low cost')
        raise InsuranceAmountError(f'Too low cost {car_price}')
    summa = car_price * RATE / 100
    return summa


# nissan_leaf_cost = -3000
#
#
# summa = get_insurance_amount(nissan_leaf_cost)
# print(summa)
