# user_name = input("Enter your name ")
# normalized_user_input = user_name.strip().title()
# print(normalized_user_input)
#
# user_surname = input("Enter your surname ")
# normalized_user_input = user_surname.strip().title()
# print(normalized_user_input)
#
#
# def get_normalized_print(message):
#     user_name = input(message)
#     normalized_user_input = user_name.strip().title()
#     print(normalized_user_input)
#     print(f'довжина {len(normalized_user_input)}')
# #
# #
# # get_normalized_print("Enter your name ")
# # get_normalized_print("Enter your surname ")
# # get_normalized_print("Enter your surname 4")
#
#
def add_two_numbers(number_1, number_2):
    result = number_1 + number_2
    return result
#
# # True
# # False
# def can_you_swim(answer):
#     positive_part = 'yes'
#     result = positive_part in answer.lower()
#     return result
#
#
# print(can_you_swim('ye s'))
#
#
# result = add_two_numbers(2, 6)
#
# print(result)


def divide_two_numbers(divided, divider):
    """divider must be not equal to zero"""
    result = divided / divider
    return result


def count_equation(first_add_number, second_add_number, divider):
    summa = add_two_numbers(first_add_number, second_add_number)
    division_result = divide_two_numbers(summa, divider)
    return division_result


result = count_equation(1, 2, 3)
result = count_equation(22, 2, 3)
print(result)

divide_two_numbers(6, 2)
