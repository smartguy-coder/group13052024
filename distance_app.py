from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js

MSG_WELCOME = 'Вітаємо в супер прозі по обчисленню площі прямокутного трикутника'
MSG_THANKS = "Дякуємо за користування"


def get_triangle_area(catet1: int | float, catet2: int | float) -> int | float:
    result = (catet1 * catet2) / 2
    return result


def get_formatted_html_h2(message: str) -> str:
    result_h2 = f'<h2>{message}</h2>'
    return result_h2


def convert_string_to_number(string_like_number: str) -> float | int:
    if string_like_number.isdigit():
        result = int(string_like_number)
    is_only_one_dot_in_string = string_like_number.count('.') == 1
    is_only_digits_except_dots = string_like_number.replace('.', '').isdigit()
    if is_only_one_dot_in_string and is_only_digits_except_dots:
        result = float(string_like_number)
    return result


def main():
    put_html(
        get_formatted_html_h2(MSG_WELCOME)
    )
    catet_1 = input_pw('Введіть довжину першого катета', type=FLOAT)
    catet_2 = input_pw('Введіть довжину другого катета', type=FLOAT)
    triangle_area = get_triangle_area(catet_1, catet_2)

    put_text(triangle_area)
    put_html(
        get_formatted_html_h2(MSG_THANKS)
    )
    run_js('setTimeout(function(){location.reload();}, 6000)')


if __name__ == '__main__':
    start_server(main, port=11000)
